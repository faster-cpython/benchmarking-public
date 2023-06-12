
# Results vs. 3.11.0

- fork: python
- ref: v3.12.0b1
- machine: darwin-arm64
- commit hash: 5612078
- commit date: 2023-05-22
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 170 ms: 1.05x slower                                       |
| docutils       | 1.47 sec                                               | 1.55 sec: 1.05x slower                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 284 ms: 1.01x slower                                       |
| nbody          | 65.6 ms                                                | 68.6 ms: 1.05x slower                                      |
| float          | 53.0 ms                                                | 58.7 ms: 1.11x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.57 ms: 1.02x faster                                      |
| regex_v8       | 16.1 ms                                                | 15.8 ms: 1.02x faster                                      |
| regex_compile  | 76.7 ms                                                | 75.7 ms: 1.01x faster                                      |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.48 ms: 1.18x faster                                      |
| unpickle_pure_python | 159 us                                                 | 146 us: 1.09x faster                                       |
| pickle_pure_python   | 201 us                                                 | 188 us: 1.06x faster                                       |
| tomli_loads          | 1.47 sec                                               | 1.39 sec: 1.05x faster                                     |
| unpickle             | 9.67 us                                                | 9.23 us: 1.05x faster                                      |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.01x slower                                       |
| pickle_dict          | 18.0 us                                                | 18.1 us: 1.01x slower                                      |
| pickle_list          | 2.81 us                                                | 2.88 us: 1.02x slower                                      |
| pickle               | 7.15 us                                                | 7.50 us: 1.05x slower                                      |
| xml_etree_iterparse  | 70.1 ms                                                | 75.2 ms: 1.07x slower                                      |
| json_loads           | 16.1 us                                                | 17.5 us: 1.09x slower                                      |
| xml_etree_process    | 35.1 ms                                                | 39.3 ms: 1.12x slower                                      |
| xml_etree_generate   | 48.3 ms                                                | 56.5 ms: 1.17x slower                                      |
| unpickle_list        | 2.65 us                                                | 3.20 us: 1.21x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 11.9 ms: 1.04x faster                                      |
| python_startup_no_site | 10.2 ms                                                | 9.76 ms: 1.04x faster                                      |
| Geometric mean         | (ref)                                                  | 1.04x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.51 ms: 1.14x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 88.7 us: 3.79x faster                                      |
| asyncio_tcp              | 651 ms                                                 | 439 ms: 1.48x faster                                       |
| json_dumps               | 7.63 ms                                                | 6.48 ms: 1.18x faster                                      |
| unpack_sequence          | 34.1 ns                                                | 29.3 ns: 1.16x faster                                      |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.25 sec: 1.15x faster                                     |
| mako                     | 8.53 ms                                                | 7.51 ms: 1.14x faster                                      |
| coverage                 | 58.4 ms                                                | 51.5 ms: 1.14x faster                                      |
| richards_super           | 39.2 ms                                                | 35.0 ms: 1.12x faster                                      |
| hexiom                   | 4.72 ms                                                | 4.21 ms: 1.12x faster                                      |
| async_tree_none          | 286 ms                                                 | 261 ms: 1.09x faster                                       |
| generators               | 28.8 ms                                                | 26.3 ms: 1.09x faster                                      |
| unpickle_pure_python     | 159 us                                                 | 146 us: 1.09x faster                                       |
| async_tree_memoization   | 336 ms                                                 | 308 ms: 1.09x faster                                       |
| deltablue                | 2.81 ms                                                | 2.59 ms: 1.09x faster                                      |
| chaos                    | 49.4 ms                                                | 46.3 ms: 1.07x faster                                      |
| deepcopy_memo            | 26.3 us                                                | 24.7 us: 1.07x faster                                      |
| sqlglot_parse            | 959 us                                                 | 901 us: 1.06x faster                                       |
| pickle_pure_python       | 201 us                                                 | 188 us: 1.06x faster                                       |
| async_tree_io            | 704 ms                                                 | 666 ms: 1.06x faster                                       |
| tomli_loads              | 1.47 sec                                               | 1.39 sec: 1.05x faster                                     |
| unpickle                 | 9.67 us                                                | 9.23 us: 1.05x faster                                      |
| sqlglot_transpile        | 1.12 ms                                                | 1.08 ms: 1.04x faster                                      |
| python_startup           | 12.4 ms                                                | 11.9 ms: 1.04x faster                                      |
| python_startup_no_site   | 10.2 ms                                                | 9.76 ms: 1.04x faster                                      |
| sqlalchemy_imperative    | 7.20 ms                                                | 6.96 ms: 1.03x faster                                      |
| richards                 | 32.2 ms                                                | 31.2 ms: 1.03x faster                                      |
| pycparser                | 698 ms                                                 | 676 ms: 1.03x faster                                       |
| create_gc_cycles         | 716 us                                                 | 698 us: 1.03x faster                                       |
| regex_effbot             | 2.63 ms                                                | 2.57 ms: 1.02x faster                                      |
| go                       | 109 ms                                                 | 106 ms: 1.02x faster                                       |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 523 ms: 1.02x faster                                       |
| regex_v8                 | 16.1 ms                                                | 15.8 ms: 1.02x faster                                      |
| mypy2                    | 195 ms                                                 | 192 ms: 1.02x faster                                       |
| regex_compile            | 76.7 ms                                                | 75.7 ms: 1.01x faster                                      |
| regex_dna                | 152 ms                                                 | 150 ms: 1.01x faster                                       |
| coroutines               | 17.8 ms                                                | 17.6 ms: 1.01x faster                                      |
| gc_traversal             | 2.42 ms                                                | 2.39 ms: 1.01x faster                                      |
| comprehensions           | 16.1 us                                                | 16.0 us: 1.01x faster                                      |
| dulwich_log              | 30.3 ms                                                | 30.2 ms: 1.00x faster                                      |
| fannkuch                 | 261 ms                                                 | 260 ms: 1.00x faster                                       |
| meteor_contest           | 73.5 ms                                                | 73.5 ms: 1.00x faster                                      |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.20 ms: 1.00x slower                                      |
| crypto_pyaes             | 51.7 ms                                                | 51.9 ms: 1.00x slower                                      |
| logging_silent           | 68.1 ns                                                | 68.3 ns: 1.00x slower                                      |
| scimark_fft              | 200 ms                                                 | 201 ms: 1.01x slower                                       |
| xml_etree_parse          | 108 ms                                                 | 109 ms: 1.01x slower                                       |
| pickle_dict              | 18.0 us                                                | 18.1 us: 1.01x slower                                      |
| pidigits                 | 281 ms                                                 | 284 ms: 1.01x slower                                       |
| deepcopy                 | 223 us                                                 | 226 us: 1.01x slower                                       |
| nqueens                  | 59.8 ms                                                | 60.6 ms: 1.01x slower                                      |
| pickle_list              | 2.81 us                                                | 2.88 us: 1.02x slower                                      |
| bench_mp_pool            | 43.9 ms                                                | 45.1 ms: 1.03x slower                                      |
| scimark_lu               | 73.3 ms                                                | 75.5 ms: 1.03x slower                                      |
| nbody                    | 65.6 ms                                                | 68.6 ms: 1.05x slower                                      |
| pickle                   | 7.15 us                                                | 7.50 us: 1.05x slower                                      |
| docutils                 | 1.47 sec                                               | 1.55 sec: 1.05x slower                                     |
| sqlalchemy_declarative   | 62.6 ms                                                | 65.9 ms: 1.05x slower                                      |
| 2to3                     | 161 ms                                                 | 170 ms: 1.05x slower                                       |
| spectral_norm            | 72.6 ms                                                | 76.5 ms: 1.05x slower                                      |
| logging_simple           | 3.55 us                                                | 3.75 us: 1.06x slower                                      |
| logging_format           | 3.78 us                                                | 4.03 us: 1.07x slower                                      |
| pyflate                  | 310 ms                                                 | 331 ms: 1.07x slower                                       |
| deepcopy_reduce          | 1.91 us                                                | 2.04 us: 1.07x slower                                      |
| xml_etree_iterparse      | 70.1 ms                                                | 75.2 ms: 1.07x slower                                      |
| pprint_pformat           | 954 ms                                                 | 1.03 sec: 1.08x slower                                     |
| mdp                      | 1.55 sec                                               | 1.67 sec: 1.08x slower                                     |
| json_loads               | 16.1 us                                                | 17.5 us: 1.09x slower                                      |
| pprint_safe_repr         | 466 ms                                                 | 508 ms: 1.09x slower                                       |
| json                     | 2.78 ms                                                | 3.03 ms: 1.09x slower                                      |
| scimark_monte_carlo      | 46.5 ms                                                | 50.9 ms: 1.09x slower                                      |
| sqlglot_normalize        | 171 ms                                                 | 188 ms: 1.10x slower                                       |
| pathlib                  | 27.2 ms                                                | 30.1 ms: 1.11x slower                                      |
| float                    | 53.0 ms                                                | 58.7 ms: 1.11x slower                                      |
| xml_etree_process        | 35.1 ms                                                | 39.3 ms: 1.12x slower                                      |
| sqlglot_optimize         | 31.1 ms                                                | 35.0 ms: 1.12x slower                                      |
| telco                    | 3.41 ms                                                | 3.88 ms: 1.14x slower                                      |
| scimark_sor              | 82.6 ms                                                | 94.4 ms: 1.14x slower                                      |
| xml_etree_generate       | 48.3 ms                                                | 56.5 ms: 1.17x slower                                      |
| unpickle_list            | 2.65 us                                                | 3.20 us: 1.21x slower                                      |
| raytrace                 | 207 ms                                                 | 251 ms: 1.21x slower                                       |
| sqlite_synth             | 1.27 us                                                | 1.55 us: 1.22x slower                                      |
| async_generators         | 196 ms                                                 | 314 ms: 1.60x slower                                       |
| Geometric mean           | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (2): tornado_http, bench_thread_pool
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230522-3.12.0b1-5612078/bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078.json: dask
