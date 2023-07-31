
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: darwin-arm64
- commit hash: e3b5ed7
- commit date: 2023-07-29
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 167 ms: 1.04x slower                                   |
| docutils       | 1.47 sec                                               | 1.50 sec: 1.02x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                   |
| nbody          | 65.6 ms                                                | 69.0 ms: 1.05x slower                                  |
| float          | 53.0 ms                                                | 56.3 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.57 ms: 1.02x faster                                  |
| regex_v8       | 16.1 ms                                                | 15.8 ms: 1.02x faster                                  |
| regex_compile  | 76.7 ms                                                | 75.6 ms: 1.02x faster                                  |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.32 ms: 1.21x faster                                  |
| unpickle_pure_python | 159 us                                                 | 145 us: 1.10x faster                                   |
| pickle_pure_python   | 201 us                                                 | 189 us: 1.06x faster                                   |
| tomli_loads          | 1.47 sec                                               | 1.39 sec: 1.06x faster                                 |
| unpickle             | 9.67 us                                                | 9.27 us: 1.04x faster                                  |
| pickle_dict          | 18.0 us                                                | 17.9 us: 1.00x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                   |
| pickle_list          | 2.81 us                                                | 2.89 us: 1.03x slower                                  |
| pickle               | 7.15 us                                                | 7.36 us: 1.03x slower                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 74.4 ms: 1.06x slower                                  |
| json_loads           | 16.1 us                                                | 17.5 us: 1.09x slower                                  |
| xml_etree_process    | 35.1 ms                                                | 38.7 ms: 1.10x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 56.0 ms: 1.16x slower                                  |
| unpickle_list        | 2.65 us                                                | 3.27 us: 1.23x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 8.42 ms: 1.21x faster                                  |
| python_startup         | 12.4 ms                                                | 10.5 ms: 1.18x faster                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.61 ms: 1.12x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 90.7 us: 3.70x faster                                  |
| asyncio_tcp              | 651 ms                                                 | 440 ms: 1.48x faster                                   |
| python_startup_no_site   | 10.2 ms                                                | 8.42 ms: 1.21x faster                                  |
| json_dumps               | 7.63 ms                                                | 6.32 ms: 1.21x faster                                  |
| chaos                    | 49.4 ms                                                | 41.7 ms: 1.18x faster                                  |
| python_startup           | 12.4 ms                                                | 10.5 ms: 1.18x faster                                  |
| deltablue                | 2.81 ms                                                | 2.40 ms: 1.17x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 29.1 ns: 1.17x faster                                  |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.23 sec: 1.17x faster                                 |
| sqlglot_parse            | 959 us                                                 | 827 us: 1.16x faster                                   |
| go                       | 109 ms                                                 | 94.0 ms: 1.15x faster                                  |
| richards_super           | 39.2 ms                                                | 34.0 ms: 1.15x faster                                  |
| coverage                 | 58.4 ms                                                | 50.7 ms: 1.15x faster                                  |
| hexiom                   | 4.72 ms                                                | 4.19 ms: 1.13x faster                                  |
| sqlglot_transpile        | 1.12 ms                                                | 1000 us: 1.12x faster                                  |
| mako                     | 8.53 ms                                                | 7.61 ms: 1.12x faster                                  |
| generators               | 28.8 ms                                                | 26.0 ms: 1.11x faster                                  |
| async_tree_none          | 286 ms                                                 | 260 ms: 1.10x faster                                   |
| unpickle_pure_python     | 159 us                                                 | 145 us: 1.10x faster                                   |
| async_tree_memoization   | 336 ms                                                 | 306 ms: 1.10x faster                                   |
| async_tree_io            | 704 ms                                                 | 651 ms: 1.08x faster                                   |
| scimark_monte_carlo      | 46.5 ms                                                | 43.4 ms: 1.07x faster                                  |
| comprehensions           | 16.1 us                                                | 15.0 us: 1.07x faster                                  |
| richards                 | 32.2 ms                                                | 30.3 ms: 1.06x faster                                  |
| deepcopy_memo            | 26.3 us                                                | 24.7 us: 1.06x faster                                  |
| pickle_pure_python       | 201 us                                                 | 189 us: 1.06x faster                                   |
| tomli_loads              | 1.47 sec                                               | 1.39 sec: 1.06x faster                                 |
| pycparser                | 698 ms                                                 | 666 ms: 1.05x faster                                   |
| unpickle                 | 9.67 us                                                | 9.27 us: 1.04x faster                                  |
| sqlalchemy_imperative    | 7.20 ms                                                | 6.92 ms: 1.04x faster                                  |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 520 ms: 1.03x faster                                   |
| regex_effbot             | 2.63 ms                                                | 2.57 ms: 1.02x faster                                  |
| coroutines               | 17.8 ms                                                | 17.4 ms: 1.02x faster                                  |
| create_gc_cycles         | 716 us                                                 | 701 us: 1.02x faster                                   |
| regex_v8                 | 16.1 ms                                                | 15.8 ms: 1.02x faster                                  |
| regex_compile            | 76.7 ms                                                | 75.6 ms: 1.02x faster                                  |
| scimark_lu               | 73.3 ms                                                | 72.2 ms: 1.02x faster                                  |
| regex_dna                | 152 ms                                                 | 150 ms: 1.01x faster                                   |
| dulwich_log              | 30.3 ms                                                | 30.0 ms: 1.01x faster                                  |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.16 ms: 1.01x faster                                  |
| pyflate                  | 310 ms                                                 | 307 ms: 1.01x faster                                   |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                  |
| nqueens                  | 59.8 ms                                                | 59.4 ms: 1.01x faster                                  |
| raytrace                 | 207 ms                                                 | 206 ms: 1.00x faster                                   |
| crypto_pyaes             | 51.7 ms                                                | 51.5 ms: 1.00x faster                                  |
| pickle_dict              | 18.0 us                                                | 17.9 us: 1.00x faster                                  |
| logging_silent           | 68.1 ns                                                | 67.9 ns: 1.00x faster                                  |
| meteor_contest           | 73.5 ms                                                | 73.8 ms: 1.00x slower                                  |
| pidigits                 | 281 ms                                                 | 282 ms: 1.01x slower                                   |
| deepcopy                 | 223 us                                                 | 224 us: 1.01x slower                                   |
| logging_format           | 3.78 us                                                | 3.84 us: 1.02x slower                                  |
| fannkuch                 | 261 ms                                                 | 266 ms: 1.02x slower                                   |
| docutils                 | 1.47 sec                                               | 1.50 sec: 1.02x slower                                 |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                   |
| bench_thread_pool        | 474 us                                                 | 485 us: 1.02x slower                                   |
| spectral_norm            | 72.6 ms                                                | 74.6 ms: 1.03x slower                                  |
| pickle_list              | 2.81 us                                                | 2.89 us: 1.03x slower                                  |
| sqlalchemy_declarative   | 62.6 ms                                                | 64.5 ms: 1.03x slower                                  |
| pickle                   | 7.15 us                                                | 7.36 us: 1.03x slower                                  |
| scimark_sor              | 82.6 ms                                                | 85.4 ms: 1.03x slower                                  |
| 2to3                     | 161 ms                                                 | 167 ms: 1.04x slower                                   |
| mdp                      | 1.55 sec                                               | 1.62 sec: 1.05x slower                                 |
| nbody                    | 65.6 ms                                                | 69.0 ms: 1.05x slower                                  |
| xml_etree_iterparse      | 70.1 ms                                                | 74.4 ms: 1.06x slower                                  |
| float                    | 53.0 ms                                                | 56.3 ms: 1.06x slower                                  |
| deepcopy_reduce          | 1.91 us                                                | 2.04 us: 1.07x slower                                  |
| pprint_pformat           | 954 ms                                                 | 1.02 sec: 1.07x slower                                 |
| json                     | 2.78 ms                                                | 2.97 ms: 1.07x slower                                  |
| pathlib                  | 27.2 ms                                                | 29.2 ms: 1.07x slower                                  |
| pprint_safe_repr         | 466 ms                                                 | 502 ms: 1.08x slower                                   |
| sqlglot_normalize        | 171 ms                                                 | 184 ms: 1.08x slower                                   |
| json_loads               | 16.1 us                                                | 17.5 us: 1.09x slower                                  |
| telco                    | 3.41 ms                                                | 3.71 ms: 1.09x slower                                  |
| sqlglot_optimize         | 31.1 ms                                                | 33.9 ms: 1.09x slower                                  |
| xml_etree_process        | 35.1 ms                                                | 38.7 ms: 1.10x slower                                  |
| xml_etree_generate       | 48.3 ms                                                | 56.0 ms: 1.16x slower                                  |
| unpickle_list            | 2.65 us                                                | 3.27 us: 1.23x slower                                  |
| sqlite_synth             | 1.27 us                                                | 1.61 us: 1.27x slower                                  |
| mypy2                    | 195 ms                                                 | 255 ms: 1.31x slower                                   |
| async_generators         | 196 ms                                                 | 306 ms: 1.56x slower                                   |
| Geometric mean           | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (4): tornado_http, scimark_fft, logging_simple, bench_mp_pool
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230729-3.12.0b4+-e3b5ed7/bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7.json: dask
