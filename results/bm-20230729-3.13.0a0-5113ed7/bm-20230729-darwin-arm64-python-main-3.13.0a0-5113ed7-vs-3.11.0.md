
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 5113ed7
- commit date: 2023-07-29
- overall geometric mean: 1.03x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.56 sec: 1.06x slower                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| nbody          | 65.6 ms                                                | 72.8 ms: 1.11x slower                                 |
| float          | 53.0 ms                                                | 60.4 ms: 1.14x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                 |
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| regex_compile  | 76.7 ms                                                | 81.5 ms: 1.06x slower                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.61 ms: 1.15x faster                                 |
| unpickle             | 9.67 us                                                | 9.30 us: 1.04x faster                                 |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                  |
| pickle_pure_python   | 201 us                                                 | 205 us: 1.02x slower                                  |
| pickle               | 7.15 us                                                | 7.34 us: 1.03x slower                                 |
| pickle_list          | 2.81 us                                                | 2.91 us: 1.04x slower                                 |
| unpickle_pure_python | 159 us                                                 | 166 us: 1.04x slower                                  |
| json_loads           | 16.1 us                                                | 17.6 us: 1.09x slower                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 77.1 ms: 1.10x slower                                 |
| tomli_loads          | 1.47 sec                                               | 1.67 sec: 1.14x slower                                |
| xml_etree_process    | 35.1 ms                                                | 41.5 ms: 1.18x slower                                 |
| unpickle_list        | 2.65 us                                                | 3.15 us: 1.19x slower                                 |
| xml_etree_generate   | 48.3 ms                                                | 59.2 ms: 1.23x slower                                 |
| Geometric mean       | (ref)                                                  | 1.06x slower                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 8.22 ms: 1.24x faster                                 |
| python_startup         | 12.4 ms                                                | 10.3 ms: 1.21x faster                                 |
| Geometric mean         | (ref)                                                  | 1.22x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.82 ms: 1.09x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 96.4 us: 3.48x faster                                 |
| asyncio_tcp              | 651 ms                                                 | 407 ms: 1.60x faster                                  |
| python_startup_no_site   | 10.2 ms                                                | 8.22 ms: 1.24x faster                                 |
| python_startup           | 12.4 ms                                                | 10.3 ms: 1.21x faster                                 |
| unpack_sequence          | 34.1 ns                                                | 28.2 ns: 1.21x faster                                 |
| json_dumps               | 7.63 ms                                                | 6.61 ms: 1.15x faster                                 |
| chaos                    | 49.4 ms                                                | 43.3 ms: 1.14x faster                                 |
| coverage                 | 58.4 ms                                                | 51.8 ms: 1.13x faster                                 |
| mako                     | 8.53 ms                                                | 7.82 ms: 1.09x faster                                 |
| crypto_pyaes             | 51.7 ms                                                | 48.7 ms: 1.06x faster                                 |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.36 sec: 1.06x faster                                |
| async_tree_none          | 286 ms                                                 | 274 ms: 1.04x faster                                  |
| unpickle                 | 9.67 us                                                | 9.30 us: 1.04x faster                                 |
| async_tree_memoization   | 336 ms                                                 | 324 ms: 1.03x faster                                  |
| create_gc_cycles         | 716 us                                                 | 693 us: 1.03x faster                                  |
| sqlglot_parse            | 959 us                                                 | 931 us: 1.03x faster                                  |
| async_tree_io            | 704 ms                                                 | 685 ms: 1.03x faster                                  |
| regex_effbot             | 2.63 ms                                                | 2.56 ms: 1.03x faster                                 |
| generators               | 28.8 ms                                                | 28.0 ms: 1.03x faster                                 |
| regex_v8                 | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| regex_dna                | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| sqlglot_transpile        | 1.12 ms                                                | 1.11 ms: 1.01x faster                                 |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                 |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| hexiom                   | 4.72 ms                                                | 4.78 ms: 1.01x slower                                 |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.24 ms: 1.01x slower                                 |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                  |
| pycparser                | 698 ms                                                 | 711 ms: 1.02x slower                                  |
| pickle_pure_python       | 201 us                                                 | 205 us: 1.02x slower                                  |
| pickle                   | 7.15 us                                                | 7.34 us: 1.03x slower                                 |
| scimark_fft              | 200 ms                                                 | 206 ms: 1.03x slower                                  |
| deltablue                | 2.81 ms                                                | 2.91 ms: 1.03x slower                                 |
| pickle_list              | 2.81 us                                                | 2.91 us: 1.04x slower                                 |
| comprehensions           | 16.1 us                                                | 16.8 us: 1.04x slower                                 |
| deepcopy_memo            | 26.3 us                                                | 27.4 us: 1.04x slower                                 |
| unpickle_pure_python     | 159 us                                                 | 166 us: 1.04x slower                                  |
| dulwich_log              | 30.3 ms                                                | 31.7 ms: 1.05x slower                                 |
| spectral_norm            | 72.6 ms                                                | 76.1 ms: 1.05x slower                                 |
| meteor_contest           | 73.5 ms                                                | 77.3 ms: 1.05x slower                                 |
| richards_super           | 39.2 ms                                                | 41.2 ms: 1.05x slower                                 |
| docutils                 | 1.47 sec                                               | 1.56 sec: 1.06x slower                                |
| regex_compile            | 76.7 ms                                                | 81.5 ms: 1.06x slower                                 |
| scimark_lu               | 73.3 ms                                                | 77.8 ms: 1.06x slower                                 |
| nqueens                  | 59.8 ms                                                | 63.5 ms: 1.06x slower                                 |
| bench_thread_pool        | 474 us                                                 | 507 us: 1.07x slower                                  |
| json                     | 2.78 ms                                                | 3.00 ms: 1.08x slower                                 |
| deepcopy                 | 223 us                                                 | 242 us: 1.09x slower                                  |
| json_loads               | 16.1 us                                                | 17.6 us: 1.09x slower                                 |
| mdp                      | 1.55 sec                                               | 1.69 sec: 1.09x slower                                |
| pathlib                  | 27.2 ms                                                | 29.8 ms: 1.09x slower                                 |
| coroutines               | 17.8 ms                                                | 19.4 ms: 1.09x slower                                 |
| xml_etree_iterparse      | 70.1 ms                                                | 77.1 ms: 1.10x slower                                 |
| logging_simple           | 3.55 us                                                | 3.91 us: 1.10x slower                                 |
| nbody                    | 65.6 ms                                                | 72.8 ms: 1.11x slower                                 |
| fannkuch                 | 261 ms                                                 | 290 ms: 1.11x slower                                  |
| raytrace                 | 207 ms                                                 | 230 ms: 1.11x slower                                  |
| logging_format           | 3.78 us                                                | 4.21 us: 1.11x slower                                 |
| go                       | 109 ms                                                 | 122 ms: 1.12x slower                                  |
| deepcopy_reduce          | 1.91 us                                                | 2.15 us: 1.13x slower                                 |
| sqlglot_normalize        | 171 ms                                                 | 194 ms: 1.13x slower                                  |
| pprint_pformat           | 954 ms                                                 | 1.08 sec: 1.13x slower                                |
| tomli_loads              | 1.47 sec                                               | 1.67 sec: 1.14x slower                                |
| pprint_safe_repr         | 466 ms                                                 | 531 ms: 1.14x slower                                  |
| float                    | 53.0 ms                                                | 60.4 ms: 1.14x slower                                 |
| sqlglot_optimize         | 31.1 ms                                                | 35.9 ms: 1.16x slower                                 |
| richards                 | 32.2 ms                                                | 37.6 ms: 1.17x slower                                 |
| scimark_monte_carlo      | 46.5 ms                                                | 54.5 ms: 1.17x slower                                 |
| pyflate                  | 310 ms                                                 | 365 ms: 1.18x slower                                  |
| xml_etree_process        | 35.1 ms                                                | 41.5 ms: 1.18x slower                                 |
| logging_silent           | 68.1 ns                                                | 80.6 ns: 1.18x slower                                 |
| unpickle_list            | 2.65 us                                                | 3.15 us: 1.19x slower                                 |
| xml_etree_generate       | 48.3 ms                                                | 59.2 ms: 1.23x slower                                 |
| sqlite_synth             | 1.27 us                                                | 1.61 us: 1.27x slower                                 |
| telco                    | 3.41 ms                                                | 4.58 ms: 1.34x slower                                 |
| mypy2                    | 195 ms                                                 | 263 ms: 1.35x slower                                  |
| scimark_sor              | 82.6 ms                                                | 120 ms: 1.45x slower                                  |
| async_generators         | 196 ms                                                 | 316 ms: 1.61x slower                                  |
| Geometric mean           | (ref)                                                  | 1.03x slower                                          |

Benchmark hidden because not significant (4): pickle_dict, bench_mp_pool, async_tree_cpu_io_mixed, tornado_http
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230729-3.13.0a0-5113ed7/bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7.json: dask


# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x
