
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3a314f7
- commit date: 2023-06-10
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.54 sec: 1.05x slower                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| float          | 53.0 ms                                                | 56.6 ms: 1.07x slower                                 |
| nbody          | 65.6 ms                                                | 71.6 ms: 1.09x slower                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| regex_compile  | 76.7 ms                                                | 75.9 ms: 1.01x faster                                 |
| regex_dna      | 152 ms                                                 | 151 ms: 1.01x faster                                  |
| regex_effbot   | 2.63 ms                                                | 2.62 ms: 1.00x faster                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.55 ms: 1.16x faster                                 |
| unpickle_pure_python | 159 us                                                 | 145 us: 1.09x faster                                  |
| pickle_pure_python   | 201 us                                                 | 186 us: 1.08x faster                                  |
| tomli_loads          | 1.47 sec                                               | 1.39 sec: 1.05x faster                                |
| unpickle             | 9.67 us                                                | 9.33 us: 1.04x faster                                 |
| pickle_dict          | 18.0 us                                                | 17.9 us: 1.00x faster                                 |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.02x slower                                  |
| pickle_list          | 2.81 us                                                | 2.91 us: 1.03x slower                                 |
| pickle               | 7.15 us                                                | 7.42 us: 1.04x slower                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 74.9 ms: 1.07x slower                                 |
| json_loads           | 16.1 us                                                | 17.6 us: 1.10x slower                                 |
| xml_etree_process    | 35.1 ms                                                | 38.9 ms: 1.11x slower                                 |
| xml_etree_generate   | 48.3 ms                                                | 56.3 ms: 1.17x slower                                 |
| unpickle_list        | 2.65 us                                                | 3.20 us: 1.21x slower                                 |
| Geometric mean       | (ref)                                                  | 1.02x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 11.7 ms: 1.06x faster                                 |
| python_startup_no_site | 10.2 ms                                                | 9.66 ms: 1.05x faster                                 |
| Geometric mean         | (ref)                                                  | 1.06x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.55 ms: 1.13x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 91.1 us: 3.69x faster                                 |
| asyncio_tcp              | 651 ms                                                 | 439 ms: 1.48x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 27.8 ns: 1.23x faster                                 |
| sqlglot_parse            | 959 us                                                 | 823 us: 1.16x faster                                  |
| json_dumps               | 7.63 ms                                                | 6.55 ms: 1.16x faster                                 |
| deltablue                | 2.81 ms                                                | 2.43 ms: 1.16x faster                                 |
| coverage                 | 58.4 ms                                                | 50.6 ms: 1.16x faster                                 |
| mako                     | 8.53 ms                                                | 7.55 ms: 1.13x faster                                 |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.27 sec: 1.13x faster                                |
| chaos                    | 49.4 ms                                                | 43.9 ms: 1.13x faster                                 |
| richards_super           | 39.2 ms                                                | 34.8 ms: 1.13x faster                                 |
| go                       | 109 ms                                                 | 96.5 ms: 1.13x faster                                 |
| sqlglot_transpile        | 1.12 ms                                                | 998 us: 1.12x faster                                  |
| hexiom                   | 4.72 ms                                                | 4.23 ms: 1.11x faster                                 |
| generators               | 28.8 ms                                                | 26.0 ms: 1.11x faster                                 |
| unpickle_pure_python     | 159 us                                                 | 145 us: 1.09x faster                                  |
| pickle_pure_python       | 201 us                                                 | 186 us: 1.08x faster                                  |
| python_startup           | 12.4 ms                                                | 11.7 ms: 1.06x faster                                 |
| tomli_loads              | 1.47 sec                                               | 1.39 sec: 1.05x faster                                |
| python_startup_no_site   | 10.2 ms                                                | 9.66 ms: 1.05x faster                                 |
| unpickle                 | 9.67 us                                                | 9.33 us: 1.04x faster                                 |
| deepcopy_memo            | 26.3 us                                                | 25.4 us: 1.03x faster                                 |
| richards                 | 32.2 ms                                                | 31.2 ms: 1.03x faster                                 |
| regex_v8                 | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| coroutines               | 17.8 ms                                                | 17.3 ms: 1.03x faster                                 |
| pycparser                | 698 ms                                                 | 680 ms: 1.03x faster                                  |
| async_tree_memoization   | 336 ms                                                 | 328 ms: 1.02x faster                                  |
| logging_silent           | 68.1 ns                                                | 66.6 ns: 1.02x faster                                 |
| async_tree_none          | 286 ms                                                 | 280 ms: 1.02x faster                                  |
| create_gc_cycles         | 716 us                                                 | 704 us: 1.02x faster                                  |
| dulwich_log              | 30.3 ms                                                | 29.9 ms: 1.01x faster                                 |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.15 ms: 1.01x faster                                 |
| regex_compile            | 76.7 ms                                                | 75.9 ms: 1.01x faster                                 |
| regex_dna                | 152 ms                                                 | 151 ms: 1.01x faster                                  |
| comprehensions           | 16.1 us                                                | 16.0 us: 1.01x faster                                 |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                 |
| async_tree_io            | 704 ms                                                 | 701 ms: 1.00x faster                                  |
| crypto_pyaes             | 51.7 ms                                                | 51.5 ms: 1.00x faster                                 |
| regex_effbot             | 2.63 ms                                                | 2.62 ms: 1.00x faster                                 |
| pickle_dict              | 18.0 us                                                | 17.9 us: 1.00x faster                                 |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| scimark_lu               | 73.3 ms                                                | 73.7 ms: 1.01x slower                                 |
| scimark_fft              | 200 ms                                                 | 202 ms: 1.01x slower                                  |
| bench_thread_pool        | 474 us                                                 | 483 us: 1.02x slower                                  |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 543 ms: 1.02x slower                                  |
| logging_simple           | 3.55 us                                                | 3.62 us: 1.02x slower                                 |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.02x slower                                  |
| spectral_norm            | 72.6 ms                                                | 74.3 ms: 1.02x slower                                 |
| scimark_sor              | 82.6 ms                                                | 84.8 ms: 1.03x slower                                 |
| bench_mp_pool            | 43.9 ms                                                | 45.2 ms: 1.03x slower                                 |
| fannkuch                 | 261 ms                                                 | 269 ms: 1.03x slower                                  |
| logging_format           | 3.78 us                                                | 3.90 us: 1.03x slower                                 |
| pickle_list              | 2.81 us                                                | 2.91 us: 1.03x slower                                 |
| pickle                   | 7.15 us                                                | 7.42 us: 1.04x slower                                 |
| deepcopy                 | 223 us                                                 | 233 us: 1.04x slower                                  |
| docutils                 | 1.47 sec                                               | 1.54 sec: 1.05x slower                                |
| mdp                      | 1.55 sec                                               | 1.62 sec: 1.05x slower                                |
| pyflate                  | 310 ms                                                 | 328 ms: 1.06x slower                                  |
| pprint_pformat           | 954 ms                                                 | 1.01 sec: 1.06x slower                                |
| pprint_safe_repr         | 466 ms                                                 | 498 ms: 1.07x slower                                  |
| xml_etree_iterparse      | 70.1 ms                                                | 74.9 ms: 1.07x slower                                 |
| float                    | 53.0 ms                                                | 56.6 ms: 1.07x slower                                 |
| json                     | 2.78 ms                                                | 2.99 ms: 1.08x slower                                 |
| sqlglot_normalize        | 171 ms                                                 | 184 ms: 1.08x slower                                  |
| scimark_monte_carlo      | 46.5 ms                                                | 50.5 ms: 1.09x slower                                 |
| nbody                    | 65.6 ms                                                | 71.6 ms: 1.09x slower                                 |
| sqlglot_optimize         | 31.1 ms                                                | 34.0 ms: 1.09x slower                                 |
| json_loads               | 16.1 us                                                | 17.6 us: 1.10x slower                                 |
| xml_etree_process        | 35.1 ms                                                | 38.9 ms: 1.11x slower                                 |
| deepcopy_reduce          | 1.91 us                                                | 2.12 us: 1.11x slower                                 |
| telco                    | 3.41 ms                                                | 3.87 ms: 1.14x slower                                 |
| pathlib                  | 27.2 ms                                                | 31.0 ms: 1.14x slower                                 |
| xml_etree_generate       | 48.3 ms                                                | 56.3 ms: 1.17x slower                                 |
| raytrace                 | 207 ms                                                 | 242 ms: 1.17x slower                                  |
| unpickle_list            | 2.65 us                                                | 3.20 us: 1.21x slower                                 |
| sqlite_synth             | 1.27 us                                                | 1.56 us: 1.23x slower                                 |
| mypy2                    | 195 ms                                                 | 258 ms: 1.32x slower                                  |
| async_generators         | 196 ms                                                 | 311 ms: 1.58x slower                                  |
| Geometric mean           | (ref)                                                  | 1.01x faster                                          |

Benchmark hidden because not significant (3): tornado_http, nqueens, meteor_contest
Ignored benchmarks (17) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
