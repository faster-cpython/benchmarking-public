
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 18b1fde
- commit date: 2023-07-01
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.57 sec: 1.07x slower                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| nbody          | 65.6 ms                                                | 72.4 ms: 1.10x slower                                 |
| float          | 53.0 ms                                                | 60.0 ms: 1.13x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| regex_effbot   | 2.63 ms                                                | 2.57 ms: 1.02x faster                                 |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                  |
| regex_compile  | 76.7 ms                                                | 80.0 ms: 1.04x slower                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.66 ms: 1.14x faster                                 |
| unpickle             | 9.67 us                                                | 9.38 us: 1.03x faster                                 |
| pickle_pure_python   | 201 us                                                 | 203 us: 1.01x slower                                  |
| unpickle_pure_python | 159 us                                                 | 162 us: 1.02x slower                                  |
| pickle_list          | 2.81 us                                                | 2.87 us: 1.02x slower                                 |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.02x slower                                  |
| pickle               | 7.15 us                                                | 7.37 us: 1.03x slower                                 |
| json_loads           | 16.1 us                                                | 17.5 us: 1.09x slower                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 76.8 ms: 1.10x slower                                 |
| tomli_loads          | 1.47 sec                                               | 1.66 sec: 1.14x slower                                |
| xml_etree_process    | 35.1 ms                                                | 41.1 ms: 1.17x slower                                 |
| unpickle_list        | 2.65 us                                                | 3.17 us: 1.20x slower                                 |
| xml_etree_generate   | 48.3 ms                                                | 58.8 ms: 1.22x slower                                 |
| Geometric mean       | (ref)                                                  | 1.06x slower                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 8.81 ms: 1.15x faster                                 |
| python_startup         | 12.4 ms                                                | 10.9 ms: 1.14x faster                                 |
| Geometric mean         | (ref)                                                  | 1.15x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.60 ms: 1.12x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 95.2 us: 3.53x faster                                 |
| asyncio_tcp              | 651 ms                                                 | 438 ms: 1.49x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 28.2 ns: 1.21x faster                                 |
| chaos                    | 49.4 ms                                                | 42.2 ms: 1.17x faster                                 |
| python_startup_no_site   | 10.2 ms                                                | 8.81 ms: 1.15x faster                                 |
| json_dumps               | 7.63 ms                                                | 6.66 ms: 1.14x faster                                 |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.26 sec: 1.14x faster                                |
| python_startup           | 12.4 ms                                                | 10.9 ms: 1.14x faster                                 |
| coverage                 | 58.4 ms                                                | 51.3 ms: 1.14x faster                                 |
| mako                     | 8.53 ms                                                | 7.60 ms: 1.12x faster                                 |
| generators               | 28.8 ms                                                | 27.2 ms: 1.06x faster                                 |
| async_tree_none          | 286 ms                                                 | 276 ms: 1.04x faster                                  |
| async_tree_memoization   | 336 ms                                                 | 325 ms: 1.03x faster                                  |
| unpickle                 | 9.67 us                                                | 9.38 us: 1.03x faster                                 |
| regex_v8                 | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| create_gc_cycles         | 716 us                                                 | 697 us: 1.03x faster                                  |
| regex_effbot             | 2.63 ms                                                | 2.57 ms: 1.02x faster                                 |
| async_tree_io            | 704 ms                                                 | 693 ms: 1.02x faster                                  |
| regex_dna                | 152 ms                                                 | 150 ms: 1.01x faster                                  |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                 |
| deepcopy_memo            | 26.3 us                                                | 26.2 us: 1.01x faster                                 |
| sqlglot_parse            | 959 us                                                 | 954 us: 1.01x faster                                  |
| hexiom                   | 4.72 ms                                                | 4.72 ms: 1.00x faster                                 |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.23 ms: 1.01x slower                                 |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 539 ms: 1.01x slower                                  |
| pickle_pure_python       | 201 us                                                 | 203 us: 1.01x slower                                  |
| crypto_pyaes             | 51.7 ms                                                | 52.5 ms: 1.01x slower                                 |
| comprehensions           | 16.1 us                                                | 16.4 us: 1.01x slower                                 |
| dulwich_log              | 30.3 ms                                                | 30.8 ms: 1.02x slower                                 |
| sqlglot_transpile        | 1.12 ms                                                | 1.14 ms: 1.02x slower                                 |
| pycparser                | 698 ms                                                 | 710 ms: 1.02x slower                                  |
| unpickle_pure_python     | 159 us                                                 | 162 us: 1.02x slower                                  |
| bench_mp_pool            | 43.9 ms                                                | 44.8 ms: 1.02x slower                                 |
| pickle_list              | 2.81 us                                                | 2.87 us: 1.02x slower                                 |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.02x slower                                  |
| deltablue                | 2.81 ms                                                | 2.88 ms: 1.02x slower                                 |
| scimark_fft              | 200 ms                                                 | 205 ms: 1.03x slower                                  |
| nqueens                  | 59.8 ms                                                | 61.5 ms: 1.03x slower                                 |
| scimark_lu               | 73.3 ms                                                | 75.6 ms: 1.03x slower                                 |
| pickle                   | 7.15 us                                                | 7.37 us: 1.03x slower                                 |
| spectral_norm            | 72.6 ms                                                | 75.2 ms: 1.04x slower                                 |
| meteor_contest           | 73.5 ms                                                | 76.6 ms: 1.04x slower                                 |
| regex_compile            | 76.7 ms                                                | 80.0 ms: 1.04x slower                                 |
| richards_super           | 39.2 ms                                                | 41.2 ms: 1.05x slower                                 |
| bench_thread_pool        | 474 us                                                 | 501 us: 1.06x slower                                  |
| deepcopy                 | 223 us                                                 | 235 us: 1.06x slower                                  |
| docutils                 | 1.47 sec                                               | 1.57 sec: 1.07x slower                                |
| json                     | 2.78 ms                                                | 3.00 ms: 1.08x slower                                 |
| raytrace                 | 207 ms                                                 | 224 ms: 1.08x slower                                  |
| coroutines               | 17.8 ms                                                | 19.3 ms: 1.09x slower                                 |
| mdp                      | 1.55 sec                                               | 1.68 sec: 1.09x slower                                |
| json_loads               | 16.1 us                                                | 17.5 us: 1.09x slower                                 |
| xml_etree_iterparse      | 70.1 ms                                                | 76.8 ms: 1.10x slower                                 |
| nbody                    | 65.6 ms                                                | 72.4 ms: 1.10x slower                                 |
| sqlglot_normalize        | 171 ms                                                 | 190 ms: 1.11x slower                                  |
| logging_simple           | 3.55 us                                                | 3.94 us: 1.11x slower                                 |
| deepcopy_reduce          | 1.91 us                                                | 2.12 us: 1.11x slower                                 |
| pprint_pformat           | 954 ms                                                 | 1.06 sec: 1.11x slower                                |
| fannkuch                 | 261 ms                                                 | 291 ms: 1.11x slower                                  |
| pprint_safe_repr         | 466 ms                                                 | 522 ms: 1.12x slower                                  |
| logging_format           | 3.78 us                                                | 4.24 us: 1.12x slower                                 |
| go                       | 109 ms                                                 | 122 ms: 1.12x slower                                  |
| float                    | 53.0 ms                                                | 60.0 ms: 1.13x slower                                 |
| sqlglot_optimize         | 31.1 ms                                                | 35.3 ms: 1.13x slower                                 |
| tomli_loads              | 1.47 sec                                               | 1.66 sec: 1.14x slower                                |
| logging_silent           | 68.1 ns                                                | 77.7 ns: 1.14x slower                                 |
| pathlib                  | 27.2 ms                                                | 31.4 ms: 1.15x slower                                 |
| richards                 | 32.2 ms                                                | 37.4 ms: 1.16x slower                                 |
| xml_etree_process        | 35.1 ms                                                | 41.1 ms: 1.17x slower                                 |
| unpickle_list            | 2.65 us                                                | 3.17 us: 1.20x slower                                 |
| pyflate                  | 310 ms                                                 | 373 ms: 1.20x slower                                  |
| xml_etree_generate       | 48.3 ms                                                | 58.8 ms: 1.22x slower                                 |
| scimark_monte_carlo      | 46.5 ms                                                | 56.7 ms: 1.22x slower                                 |
| telco                    | 3.41 ms                                                | 4.25 ms: 1.25x slower                                 |
| sqlite_synth             | 1.27 us                                                | 1.62 us: 1.27x slower                                 |
| mypy2                    | 195 ms                                                 | 265 ms: 1.36x slower                                  |
| scimark_sor              | 82.6 ms                                                | 119 ms: 1.44x slower                                  |
| async_generators         | 196 ms                                                 | 313 ms: 1.59x slower                                  |
| Geometric mean           | (ref)                                                  | 1.03x slower                                          |

Benchmark hidden because not significant (2): pickle_dict, tornado_http
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x
