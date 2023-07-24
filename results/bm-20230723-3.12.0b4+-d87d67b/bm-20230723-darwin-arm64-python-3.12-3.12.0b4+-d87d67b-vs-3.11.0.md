
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: darwin-arm64
- commit hash: d87d67b
- commit date: 2023-07-23
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 168 ms: 1.04x slower                                   |
| docutils       | 1.47 sec                                               | 1.51 sec: 1.03x slower                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| nbody          | 65.6 ms                                                | 69.6 ms: 1.06x slower                                  |
| float          | 53.0 ms                                                | 56.8 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 15.8 ms: 1.02x faster                                  |
| regex_effbot   | 2.63 ms                                                | 2.58 ms: 1.02x faster                                  |
| regex_compile  | 76.7 ms                                                | 75.9 ms: 1.01x faster                                  |
| regex_dna      | 152 ms                                                 | 151 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.35 ms: 1.20x faster                                  |
| unpickle_pure_python | 159 us                                                 | 146 us: 1.09x faster                                   |
| tomli_loads          | 1.47 sec                                               | 1.39 sec: 1.05x faster                                 |
| pickle_pure_python   | 201 us                                                 | 191 us: 1.05x faster                                   |
| unpickle             | 9.67 us                                                | 9.27 us: 1.04x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.01x slower                                   |
| pickle               | 7.15 us                                                | 7.39 us: 1.03x slower                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 75.1 ms: 1.07x slower                                  |
| json_loads           | 16.1 us                                                | 17.5 us: 1.09x slower                                  |
| xml_etree_process    | 35.1 ms                                                | 39.0 ms: 1.11x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 56.1 ms: 1.16x slower                                  |
| unpickle_list        | 2.65 us                                                | 3.16 us: 1.19x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (2): pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 8.80 ms: 1.15x faster                                  |
| python_startup         | 12.4 ms                                                | 10.9 ms: 1.14x faster                                  |
| Geometric mean         | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.59 ms: 1.12x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 90.6 us: 3.71x faster                                  |
| asyncio_tcp              | 651 ms                                                 | 459 ms: 1.42x faster                                   |
| json_dumps               | 7.63 ms                                                | 6.35 ms: 1.20x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 28.7 ns: 1.19x faster                                  |
| chaos                    | 49.4 ms                                                | 42.0 ms: 1.18x faster                                  |
| deltablue                | 2.81 ms                                                | 2.42 ms: 1.16x faster                                  |
| coverage                 | 58.4 ms                                                | 50.4 ms: 1.16x faster                                  |
| python_startup_no_site   | 10.2 ms                                                | 8.80 ms: 1.15x faster                                  |
| richards_super           | 39.2 ms                                                | 34.0 ms: 1.15x faster                                  |
| sqlglot_parse            | 959 us                                                 | 833 us: 1.15x faster                                   |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.25 sec: 1.15x faster                                 |
| go                       | 109 ms                                                 | 94.6 ms: 1.15x faster                                  |
| python_startup           | 12.4 ms                                                | 10.9 ms: 1.14x faster                                  |
| mako                     | 8.53 ms                                                | 7.59 ms: 1.12x faster                                  |
| sqlglot_transpile        | 1.12 ms                                                | 1.00 ms: 1.12x faster                                  |
| hexiom                   | 4.72 ms                                                | 4.23 ms: 1.12x faster                                  |
| unpickle_pure_python     | 159 us                                                 | 146 us: 1.09x faster                                   |
| generators               | 28.8 ms                                                | 26.5 ms: 1.09x faster                                  |
| async_tree_memoization   | 336 ms                                                 | 311 ms: 1.08x faster                                   |
| async_tree_none          | 286 ms                                                 | 265 ms: 1.08x faster                                   |
| scimark_monte_carlo      | 46.5 ms                                                | 43.3 ms: 1.07x faster                                  |
| comprehensions           | 16.1 us                                                | 15.1 us: 1.07x faster                                  |
| richards                 | 32.2 ms                                                | 30.3 ms: 1.06x faster                                  |
| async_tree_io            | 704 ms                                                 | 665 ms: 1.06x faster                                   |
| tomli_loads              | 1.47 sec                                               | 1.39 sec: 1.05x faster                                 |
| deepcopy_memo            | 26.3 us                                                | 25.1 us: 1.05x faster                                  |
| pickle_pure_python       | 201 us                                                 | 191 us: 1.05x faster                                   |
| unpickle                 | 9.67 us                                                | 9.27 us: 1.04x faster                                  |
| pycparser                | 698 ms                                                 | 671 ms: 1.04x faster                                   |
| sqlalchemy_imperative    | 7.20 ms                                                | 7.00 ms: 1.03x faster                                  |
| regex_v8                 | 16.1 ms                                                | 15.8 ms: 1.02x faster                                  |
| regex_effbot             | 2.63 ms                                                | 2.58 ms: 1.02x faster                                  |
| create_gc_cycles         | 716 us                                                 | 704 us: 1.02x faster                                   |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.15 ms: 1.01x faster                                  |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 527 ms: 1.01x faster                                   |
| regex_compile            | 76.7 ms                                                | 75.9 ms: 1.01x faster                                  |
| coroutines               | 17.8 ms                                                | 17.6 ms: 1.01x faster                                  |
| dulwich_log              | 30.3 ms                                                | 30.1 ms: 1.01x faster                                  |
| scimark_lu               | 73.3 ms                                                | 72.8 ms: 1.01x faster                                  |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                  |
| regex_dna                | 152 ms                                                 | 151 ms: 1.00x faster                                   |
| pyflate                  | 310 ms                                                 | 309 ms: 1.00x faster                                   |
| crypto_pyaes             | 51.7 ms                                                | 51.6 ms: 1.00x faster                                  |
| raytrace                 | 207 ms                                                 | 207 ms: 1.00x slower                                   |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| logging_silent           | 68.1 ns                                                | 68.6 ns: 1.01x slower                                  |
| logging_simple           | 3.55 us                                                | 3.58 us: 1.01x slower                                  |
| nqueens                  | 59.8 ms                                                | 60.4 ms: 1.01x slower                                  |
| meteor_contest           | 73.5 ms                                                | 74.4 ms: 1.01x slower                                  |
| fannkuch                 | 261 ms                                                 | 265 ms: 1.01x slower                                   |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.01x slower                                   |
| logging_format           | 3.78 us                                                | 3.86 us: 1.02x slower                                  |
| deepcopy                 | 223 us                                                 | 227 us: 1.02x slower                                   |
| bench_mp_pool            | 43.9 ms                                                | 44.9 ms: 1.02x slower                                  |
| bench_thread_pool        | 474 us                                                 | 485 us: 1.02x slower                                   |
| spectral_norm            | 72.6 ms                                                | 74.6 ms: 1.03x slower                                  |
| docutils                 | 1.47 sec                                               | 1.51 sec: 1.03x slower                                 |
| pickle                   | 7.15 us                                                | 7.39 us: 1.03x slower                                  |
| sqlalchemy_declarative   | 62.6 ms                                                | 64.9 ms: 1.04x slower                                  |
| scimark_sor              | 82.6 ms                                                | 85.7 ms: 1.04x slower                                  |
| 2to3                     | 161 ms                                                 | 168 ms: 1.04x slower                                   |
| mdp                      | 1.55 sec                                               | 1.62 sec: 1.05x slower                                 |
| pprint_pformat           | 954 ms                                                 | 1.00 sec: 1.05x slower                                 |
| pprint_safe_repr         | 466 ms                                                 | 493 ms: 1.06x slower                                   |
| nbody                    | 65.6 ms                                                | 69.6 ms: 1.06x slower                                  |
| xml_etree_iterparse      | 70.1 ms                                                | 75.1 ms: 1.07x slower                                  |
| float                    | 53.0 ms                                                | 56.8 ms: 1.07x slower                                  |
| sqlglot_normalize        | 171 ms                                                 | 184 ms: 1.08x slower                                   |
| deepcopy_reduce          | 1.91 us                                                | 2.07 us: 1.08x slower                                  |
| json_loads               | 16.1 us                                                | 17.5 us: 1.09x slower                                  |
| telco                    | 3.41 ms                                                | 3.71 ms: 1.09x slower                                  |
| json                     | 2.78 ms                                                | 3.03 ms: 1.09x slower                                  |
| sqlglot_optimize         | 31.1 ms                                                | 34.1 ms: 1.10x slower                                  |
| xml_etree_process        | 35.1 ms                                                | 39.0 ms: 1.11x slower                                  |
| xml_etree_generate       | 48.3 ms                                                | 56.1 ms: 1.16x slower                                  |
| unpickle_list            | 2.65 us                                                | 3.16 us: 1.19x slower                                  |
| pathlib                  | 27.2 ms                                                | 34.0 ms: 1.25x slower                                  |
| sqlite_synth             | 1.27 us                                                | 1.61 us: 1.27x slower                                  |
| mypy2                    | 195 ms                                                 | 259 ms: 1.33x slower                                   |
| async_generators         | 196 ms                                                 | 307 ms: 1.57x slower                                   |
| Geometric mean           | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (4): tornado_http, pickle_dict, pickle_list, scimark_fft
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230723-3.12.0b4+-d87d67b/bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b.json: dask
