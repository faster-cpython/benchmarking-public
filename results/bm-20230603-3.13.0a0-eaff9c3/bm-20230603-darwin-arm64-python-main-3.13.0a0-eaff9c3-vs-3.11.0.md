
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: eaff9c3
- commit date: 2023-06-03
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.51 sec: 1.03x slower                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| nbody          | 65.6 ms                                                | 69.0 ms: 1.05x slower                                 |
| float          | 53.0 ms                                                | 57.0 ms: 1.08x slower                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 15.9 ms: 1.01x faster                                 |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                  |
| regex_compile  | 76.7 ms                                                | 75.7 ms: 1.01x faster                                 |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.40 ms: 1.19x faster                                 |
| unpickle_pure_python | 159 us                                                 | 143 us: 1.11x faster                                  |
| pickle_pure_python   | 201 us                                                 | 187 us: 1.07x faster                                  |
| tomli_loads          | 1.47 sec                                               | 1.38 sec: 1.06x faster                                |
| unpickle             | 9.67 us                                                | 9.32 us: 1.04x faster                                 |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                 |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                  |
| pickle               | 7.15 us                                                | 7.42 us: 1.04x slower                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 74.4 ms: 1.06x slower                                 |
| json_loads           | 16.1 us                                                | 17.6 us: 1.09x slower                                 |
| xml_etree_process    | 35.1 ms                                                | 38.7 ms: 1.10x slower                                 |
| xml_etree_generate   | 48.3 ms                                                | 56.1 ms: 1.16x slower                                 |
| unpickle_list        | 2.65 us                                                | 3.16 us: 1.19x slower                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 8.97 ms: 1.13x faster                                 |
| python_startup         | 12.4 ms                                                | 11.0 ms: 1.13x faster                                 |
| Geometric mean         | (ref)                                                  | 1.13x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.55 ms: 1.13x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 90.8 us: 3.70x faster                                 |
| asyncio_tcp              | 651 ms                                                 | 470 ms: 1.39x faster                                  |
| json_dumps               | 7.63 ms                                                | 6.40 ms: 1.19x faster                                 |
| chaos                    | 49.4 ms                                                | 41.5 ms: 1.19x faster                                 |
| richards_super           | 39.2 ms                                                | 33.2 ms: 1.18x faster                                 |
| unpack_sequence          | 34.1 ns                                                | 28.9 ns: 1.18x faster                                 |
| deltablue                | 2.81 ms                                                | 2.39 ms: 1.18x faster                                 |
| sqlglot_parse            | 959 us                                                 | 821 us: 1.17x faster                                  |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.25 sec: 1.15x faster                                |
| coverage                 | 58.4 ms                                                | 50.8 ms: 1.15x faster                                 |
| go                       | 109 ms                                                 | 94.4 ms: 1.15x faster                                 |
| python_startup_no_site   | 10.2 ms                                                | 8.97 ms: 1.13x faster                                 |
| sqlglot_transpile        | 1.12 ms                                                | 993 us: 1.13x faster                                  |
| mako                     | 8.53 ms                                                | 7.55 ms: 1.13x faster                                 |
| python_startup           | 12.4 ms                                                | 11.0 ms: 1.13x faster                                 |
| hexiom                   | 4.72 ms                                                | 4.20 ms: 1.12x faster                                 |
| unpickle_pure_python     | 159 us                                                 | 143 us: 1.11x faster                                  |
| generators               | 28.8 ms                                                | 26.2 ms: 1.10x faster                                 |
| richards                 | 32.2 ms                                                | 29.8 ms: 1.08x faster                                 |
| comprehensions           | 16.1 us                                                | 15.0 us: 1.07x faster                                 |
| pickle_pure_python       | 201 us                                                 | 187 us: 1.07x faster                                  |
| scimark_monte_carlo      | 46.5 ms                                                | 43.4 ms: 1.07x faster                                 |
| tomli_loads              | 1.47 sec                                               | 1.38 sec: 1.06x faster                                |
| deepcopy_memo            | 26.3 us                                                | 25.1 us: 1.05x faster                                 |
| pycparser                | 698 ms                                                 | 671 ms: 1.04x faster                                  |
| unpickle                 | 9.67 us                                                | 9.32 us: 1.04x faster                                 |
| async_tree_memoization   | 336 ms                                                 | 325 ms: 1.03x faster                                  |
| create_gc_cycles         | 716 us                                                 | 696 us: 1.03x faster                                  |
| async_tree_none          | 286 ms                                                 | 278 ms: 1.03x faster                                  |
| coroutines               | 17.8 ms                                                | 17.5 ms: 1.02x faster                                 |
| logging_silent           | 68.1 ns                                                | 66.9 ns: 1.02x faster                                 |
| dulwich_log              | 30.3 ms                                                | 29.8 ms: 1.02x faster                                 |
| regex_v8                 | 16.1 ms                                                | 15.9 ms: 1.01x faster                                 |
| async_tree_io            | 704 ms                                                 | 695 ms: 1.01x faster                                  |
| regex_dna                | 152 ms                                                 | 150 ms: 1.01x faster                                  |
| regex_compile            | 76.7 ms                                                | 75.7 ms: 1.01x faster                                 |
| regex_effbot             | 2.63 ms                                                | 2.61 ms: 1.01x faster                                 |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                 |
| fannkuch                 | 261 ms                                                 | 260 ms: 1.00x faster                                  |
| meteor_contest           | 73.5 ms                                                | 73.5 ms: 1.00x faster                                 |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| crypto_pyaes             | 51.7 ms                                                | 51.9 ms: 1.00x slower                                 |
| logging_simple           | 3.55 us                                                | 3.57 us: 1.01x slower                                 |
| pickle_list              | 2.81 us                                                | 2.83 us: 1.01x slower                                 |
| scimark_fft              | 200 ms                                                 | 201 ms: 1.01x slower                                  |
| nqueens                  | 59.8 ms                                                | 60.5 ms: 1.01x slower                                 |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 542 ms: 1.02x slower                                  |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                  |
| bench_thread_pool        | 474 us                                                 | 482 us: 1.02x slower                                  |
| bench_mp_pool            | 43.9 ms                                                | 44.7 ms: 1.02x slower                                 |
| scimark_lu               | 73.3 ms                                                | 74.7 ms: 1.02x slower                                 |
| pyflate                  | 310 ms                                                 | 316 ms: 1.02x slower                                  |
| logging_format           | 3.78 us                                                | 3.86 us: 1.02x slower                                 |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.27 ms: 1.02x slower                                 |
| docutils                 | 1.47 sec                                               | 1.51 sec: 1.03x slower                                |
| spectral_norm            | 72.6 ms                                                | 74.7 ms: 1.03x slower                                 |
| deepcopy                 | 223 us                                                 | 230 us: 1.03x slower                                  |
| scimark_sor              | 82.6 ms                                                | 85.6 ms: 1.04x slower                                 |
| pickle                   | 7.15 us                                                | 7.42 us: 1.04x slower                                 |
| pprint_pformat           | 954 ms                                                 | 995 ms: 1.04x slower                                  |
| pprint_safe_repr         | 466 ms                                                 | 489 ms: 1.05x slower                                  |
| nbody                    | 65.6 ms                                                | 69.0 ms: 1.05x slower                                 |
| mdp                      | 1.55 sec                                               | 1.63 sec: 1.05x slower                                |
| xml_etree_iterparse      | 70.1 ms                                                | 74.4 ms: 1.06x slower                                 |
| float                    | 53.0 ms                                                | 57.0 ms: 1.08x slower                                 |
| json                     | 2.78 ms                                                | 2.99 ms: 1.08x slower                                 |
| sqlglot_normalize        | 171 ms                                                 | 184 ms: 1.08x slower                                  |
| deepcopy_reduce          | 1.91 us                                                | 2.07 us: 1.09x slower                                 |
| telco                    | 3.41 ms                                                | 3.72 ms: 1.09x slower                                 |
| json_loads               | 16.1 us                                                | 17.6 us: 1.09x slower                                 |
| sqlglot_optimize         | 31.1 ms                                                | 34.1 ms: 1.10x slower                                 |
| xml_etree_process        | 35.1 ms                                                | 38.7 ms: 1.10x slower                                 |
| xml_etree_generate       | 48.3 ms                                                | 56.1 ms: 1.16x slower                                 |
| pathlib                  | 27.2 ms                                                | 32.4 ms: 1.19x slower                                 |
| unpickle_list            | 2.65 us                                                | 3.16 us: 1.19x slower                                 |
| sqlite_synth             | 1.27 us                                                | 1.57 us: 1.23x slower                                 |
| mypy2                    | 195 ms                                                 | 258 ms: 1.32x slower                                  |
| async_generators         | 196 ms                                                 | 310 ms: 1.58x slower                                  |
| Geometric mean           | (ref)                                                  | 1.02x faster                                          |

Benchmark hidden because not significant (3): tornado_http, pickle_dict, raytrace
Ignored benchmarks (17) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
