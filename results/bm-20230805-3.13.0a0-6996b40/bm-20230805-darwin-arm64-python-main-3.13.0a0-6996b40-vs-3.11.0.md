
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 6996b40
- commit date: 2023-08-05
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.55 sec: 1.05x slower                                |
| Geometric mean | (ref)                                                  | 1.03x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| nbody          | 65.6 ms                                                | 71.9 ms: 1.10x slower                                 |
| float          | 53.0 ms                                                | 59.6 ms: 1.13x slower                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| regex_effbot   | 2.63 ms                                                | 2.58 ms: 1.02x faster                                 |
| regex_compile  | 76.7 ms                                                | 80.8 ms: 1.05x slower                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.69 ms: 1.14x faster                                 |
| unpickle             | 9.67 us                                                | 9.19 us: 1.05x faster                                 |
| pickle_dict          | 18.0 us                                                | 17.9 us: 1.00x faster                                 |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.01x slower                                  |
| pickle_pure_python   | 201 us                                                 | 203 us: 1.01x slower                                  |
| pickle               | 7.15 us                                                | 7.32 us: 1.02x slower                                 |
| pickle_list          | 2.81 us                                                | 2.89 us: 1.03x slower                                 |
| unpickle_pure_python | 159 us                                                 | 166 us: 1.04x slower                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 76.4 ms: 1.09x slower                                 |
| json_loads           | 16.1 us                                                | 17.6 us: 1.09x slower                                 |
| tomli_loads          | 1.47 sec                                               | 1.64 sec: 1.12x slower                                |
| xml_etree_process    | 35.1 ms                                                | 40.8 ms: 1.16x slower                                 |
| unpickle_list        | 2.65 us                                                | 3.15 us: 1.19x slower                                 |
| xml_etree_generate   | 48.3 ms                                                | 58.9 ms: 1.22x slower                                 |
| Geometric mean       | (ref)                                                  | 1.05x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 8.52 ms: 1.19x faster                                 |
| python_startup         | 12.4 ms                                                | 10.6 ms: 1.17x faster                                 |
| Geometric mean         | (ref)                                                  | 1.18x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.49 ms: 1.14x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 95.2 us: 3.53x faster                                 |
| asyncio_tcp              | 651 ms                                                 | 419 ms: 1.55x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 27.5 ns: 1.24x faster                                 |
| python_startup_no_site   | 10.2 ms                                                | 8.52 ms: 1.19x faster                                 |
| python_startup           | 12.4 ms                                                | 10.6 ms: 1.17x faster                                 |
| coverage                 | 58.4 ms                                                | 50.8 ms: 1.15x faster                                 |
| json_dumps               | 7.63 ms                                                | 6.69 ms: 1.14x faster                                 |
| mako                     | 8.53 ms                                                | 7.49 ms: 1.14x faster                                 |
| chaos                    | 49.4 ms                                                | 45.2 ms: 1.09x faster                                 |
| crypto_pyaes             | 51.7 ms                                                | 47.5 ms: 1.09x faster                                 |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.36 sec: 1.06x faster                                |
| unpickle                 | 9.67 us                                                | 9.19 us: 1.05x faster                                 |
| async_tree_none          | 286 ms                                                 | 273 ms: 1.04x faster                                  |
| async_tree_memoization   | 336 ms                                                 | 322 ms: 1.04x faster                                  |
| async_tree_io            | 704 ms                                                 | 677 ms: 1.04x faster                                  |
| sqlglot_parse            | 959 us                                                 | 923 us: 1.04x faster                                  |
| deepcopy_memo            | 26.3 us                                                | 25.6 us: 1.03x faster                                 |
| regex_v8                 | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| regex_dna                | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| create_gc_cycles         | 716 us                                                 | 702 us: 1.02x faster                                  |
| regex_effbot             | 2.63 ms                                                | 2.58 ms: 1.02x faster                                 |
| comprehensions           | 16.1 us                                                | 15.8 us: 1.02x faster                                 |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.15 ms: 1.01x faster                                 |
| sqlglot_transpile        | 1.12 ms                                                | 1.11 ms: 1.01x faster                                 |
| generators               | 28.8 ms                                                | 28.4 ms: 1.01x faster                                 |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                 |
| pickle_dict              | 18.0 us                                                | 17.9 us: 1.00x faster                                 |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| deltablue                | 2.81 ms                                                | 2.83 ms: 1.00x slower                                 |
| scimark_fft              | 200 ms                                                 | 201 ms: 1.01x slower                                  |
| xml_etree_parse          | 108 ms                                                 | 109 ms: 1.01x slower                                  |
| pickle_pure_python       | 201 us                                                 | 203 us: 1.01x slower                                  |
| bench_mp_pool            | 43.9 ms                                                | 44.6 ms: 1.02x slower                                 |
| pycparser                | 698 ms                                                 | 711 ms: 1.02x slower                                  |
| meteor_contest           | 73.5 ms                                                | 75.1 ms: 1.02x slower                                 |
| spectral_norm            | 72.6 ms                                                | 74.3 ms: 1.02x slower                                 |
| pickle                   | 7.15 us                                                | 7.32 us: 1.02x slower                                 |
| pickle_list              | 2.81 us                                                | 2.89 us: 1.03x slower                                 |
| deepcopy                 | 223 us                                                 | 230 us: 1.03x slower                                  |
| dulwich_log              | 30.3 ms                                                | 31.4 ms: 1.04x slower                                 |
| unpickle_pure_python     | 159 us                                                 | 166 us: 1.04x slower                                  |
| richards_super           | 39.2 ms                                                | 40.9 ms: 1.04x slower                                 |
| scimark_lu               | 73.3 ms                                                | 76.7 ms: 1.05x slower                                 |
| bench_thread_pool        | 474 us                                                 | 497 us: 1.05x slower                                  |
| hexiom                   | 4.72 ms                                                | 4.96 ms: 1.05x slower                                 |
| docutils                 | 1.47 sec                                               | 1.55 sec: 1.05x slower                                |
| regex_compile            | 76.7 ms                                                | 80.8 ms: 1.05x slower                                 |
| mdp                      | 1.55 sec                                               | 1.65 sec: 1.07x slower                                |
| json                     | 2.78 ms                                                | 2.97 ms: 1.07x slower                                 |
| pathlib                  | 27.2 ms                                                | 29.5 ms: 1.08x slower                                 |
| xml_etree_iterparse      | 70.1 ms                                                | 76.4 ms: 1.09x slower                                 |
| logging_simple           | 3.55 us                                                | 3.88 us: 1.09x slower                                 |
| json_loads               | 16.1 us                                                | 17.6 us: 1.09x slower                                 |
| fannkuch                 | 261 ms                                                 | 286 ms: 1.09x slower                                  |
| nbody                    | 65.6 ms                                                | 71.9 ms: 1.10x slower                                 |
| logging_format           | 3.78 us                                                | 4.15 us: 1.10x slower                                 |
| deepcopy_reduce          | 1.91 us                                                | 2.11 us: 1.10x slower                                 |
| go                       | 109 ms                                                 | 120 ms: 1.10x slower                                  |
| coroutines               | 17.8 ms                                                | 19.6 ms: 1.10x slower                                 |
| pprint_safe_repr         | 466 ms                                                 | 517 ms: 1.11x slower                                  |
| pprint_pformat           | 954 ms                                                 | 1.06 sec: 1.11x slower                                |
| raytrace                 | 207 ms                                                 | 230 ms: 1.11x slower                                  |
| tomli_loads              | 1.47 sec                                               | 1.64 sec: 1.12x slower                                |
| float                    | 53.0 ms                                                | 59.6 ms: 1.13x slower                                 |
| logging_silent           | 68.1 ns                                                | 77.0 ns: 1.13x slower                                 |
| sqlglot_normalize        | 171 ms                                                 | 194 ms: 1.14x slower                                  |
| scimark_monte_carlo      | 46.5 ms                                                | 52.9 ms: 1.14x slower                                 |
| richards                 | 32.2 ms                                                | 36.8 ms: 1.14x slower                                 |
| sqlglot_optimize         | 31.1 ms                                                | 35.8 ms: 1.15x slower                                 |
| pyflate                  | 310 ms                                                 | 360 ms: 1.16x slower                                  |
| xml_etree_process        | 35.1 ms                                                | 40.8 ms: 1.16x slower                                 |
| unpickle_list            | 2.65 us                                                | 3.15 us: 1.19x slower                                 |
| xml_etree_generate       | 48.3 ms                                                | 58.9 ms: 1.22x slower                                 |
| sqlite_synth             | 1.27 us                                                | 1.60 us: 1.26x slower                                 |
| mypy2                    | 195 ms                                                 | 263 ms: 1.35x slower                                  |
| telco                    | 3.41 ms                                                | 4.59 ms: 1.35x slower                                 |
| scimark_sor              | 82.6 ms                                                | 119 ms: 1.44x slower                                  |
| async_generators         | 196 ms                                                 | 311 ms: 1.59x slower                                  |
| Geometric mean           | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (3): nqueens, async_tree_cpu_io_mixed, tornado_http
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230805-3.13.0a0-6996b40/bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40.json: dask
