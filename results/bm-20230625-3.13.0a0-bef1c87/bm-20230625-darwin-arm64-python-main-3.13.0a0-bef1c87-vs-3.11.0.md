
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: bef1c87
- commit date: 2023-06-25
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.54 sec: 1.05x slower                                |
| Geometric mean | (ref)                                                  | 1.03x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 281 ms                                                 | 283 ms: 1.01x slower                                  |
| float          | 53.0 ms                                                | 57.3 ms: 1.08x slower                                 |
| nbody          | 65.6 ms                                                | 71.5 ms: 1.09x slower                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 15.6 ms: 1.03x faster                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| regex_compile  | 76.7 ms                                                | 75.4 ms: 1.02x faster                                 |
| regex_effbot   | 2.63 ms                                                | 2.59 ms: 1.02x faster                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.43 ms: 1.19x faster                                 |
| unpickle_pure_python | 159 us                                                 | 148 us: 1.08x faster                                  |
| unpickle             | 9.67 us                                                | 9.14 us: 1.06x faster                                 |
| pickle_pure_python   | 201 us                                                 | 191 us: 1.05x faster                                  |
| tomli_loads          | 1.47 sec                                               | 1.42 sec: 1.03x faster                                |
| pickle_dict          | 18.0 us                                                | 18.2 us: 1.01x slower                                 |
| pickle_list          | 2.81 us                                                | 2.86 us: 1.02x slower                                 |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                  |
| pickle               | 7.15 us                                                | 7.49 us: 1.05x slower                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 75.7 ms: 1.08x slower                                 |
| json_loads           | 16.1 us                                                | 17.7 us: 1.10x slower                                 |
| xml_etree_process    | 35.1 ms                                                | 39.2 ms: 1.12x slower                                 |
| xml_etree_generate   | 48.3 ms                                                | 56.6 ms: 1.17x slower                                 |
| unpickle_list        | 2.65 us                                                | 3.14 us: 1.18x slower                                 |
| Geometric mean       | (ref)                                                  | 1.02x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.0 ms: 1.04x faster                                 |
| python_startup_no_site | 10.2 ms                                                | 9.87 ms: 1.03x faster                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.60 ms: 1.12x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 90.8 us: 3.70x faster                                 |
| asyncio_tcp              | 651 ms                                                 | 416 ms: 1.56x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 28.2 ns: 1.21x faster                                 |
| json_dumps               | 7.63 ms                                                | 6.43 ms: 1.19x faster                                 |
| chaos                    | 49.4 ms                                                | 42.5 ms: 1.16x faster                                 |
| sqlglot_parse            | 959 us                                                 | 836 us: 1.15x faster                                  |
| coverage                 | 58.4 ms                                                | 51.0 ms: 1.15x faster                                 |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.26 sec: 1.14x faster                                |
| deltablue                | 2.81 ms                                                | 2.50 ms: 1.12x faster                                 |
| mako                     | 8.53 ms                                                | 7.60 ms: 1.12x faster                                 |
| sqlglot_transpile        | 1.12 ms                                                | 1.01 ms: 1.11x faster                                 |
| richards_super           | 39.2 ms                                                | 35.4 ms: 1.11x faster                                 |
| go                       | 109 ms                                                 | 98.5 ms: 1.10x faster                                 |
| hexiom                   | 4.72 ms                                                | 4.39 ms: 1.08x faster                                 |
| unpickle_pure_python     | 159 us                                                 | 148 us: 1.08x faster                                  |
| generators               | 28.8 ms                                                | 26.9 ms: 1.07x faster                                 |
| unpickle                 | 9.67 us                                                | 9.14 us: 1.06x faster                                 |
| async_tree_memoization   | 336 ms                                                 | 318 ms: 1.05x faster                                  |
| async_tree_none          | 286 ms                                                 | 271 ms: 1.05x faster                                  |
| pickle_pure_python       | 201 us                                                 | 191 us: 1.05x faster                                  |
| async_tree_io            | 704 ms                                                 | 673 ms: 1.05x faster                                  |
| python_startup           | 12.4 ms                                                | 12.0 ms: 1.04x faster                                 |
| regex_v8                 | 16.1 ms                                                | 15.6 ms: 1.03x faster                                 |
| python_startup_no_site   | 10.2 ms                                                | 9.87 ms: 1.03x faster                                 |
| tomli_loads              | 1.47 sec                                               | 1.42 sec: 1.03x faster                                |
| create_gc_cycles         | 716 us                                                 | 700 us: 1.02x faster                                  |
| deepcopy_memo            | 26.3 us                                                | 25.8 us: 1.02x faster                                 |
| regex_dna                | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| pycparser                | 698 ms                                                 | 685 ms: 1.02x faster                                  |
| regex_compile            | 76.7 ms                                                | 75.4 ms: 1.02x faster                                 |
| regex_effbot             | 2.63 ms                                                | 2.59 ms: 1.02x faster                                 |
| richards                 | 32.2 ms                                                | 31.8 ms: 1.01x faster                                 |
| dulwich_log              | 30.3 ms                                                | 30.0 ms: 1.01x faster                                 |
| scimark_lu               | 73.3 ms                                                | 72.7 ms: 1.01x faster                                 |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.00x faster                                 |
| comprehensions           | 16.1 us                                                | 16.2 us: 1.00x slower                                 |
| meteor_contest           | 73.5 ms                                                | 73.7 ms: 1.00x slower                                 |
| nqueens                  | 59.8 ms                                                | 60.1 ms: 1.01x slower                                 |
| pidigits                 | 281 ms                                                 | 283 ms: 1.01x slower                                  |
| pickle_dict              | 18.0 us                                                | 18.2 us: 1.01x slower                                 |
| scimark_fft              | 200 ms                                                 | 202 ms: 1.01x slower                                  |
| pickle_list              | 2.81 us                                                | 2.86 us: 1.02x slower                                 |
| logging_silent           | 68.1 ns                                                | 69.6 ns: 1.02x slower                                 |
| logging_simple           | 3.55 us                                                | 3.64 us: 1.03x slower                                 |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.03x slower                                  |
| spectral_norm            | 72.6 ms                                                | 74.7 ms: 1.03x slower                                 |
| fannkuch                 | 261 ms                                                 | 269 ms: 1.03x slower                                  |
| bench_mp_pool            | 43.9 ms                                                | 45.5 ms: 1.03x slower                                 |
| logging_format           | 3.78 us                                                | 3.91 us: 1.04x slower                                 |
| deepcopy                 | 223 us                                                 | 231 us: 1.04x slower                                  |
| bench_thread_pool        | 474 us                                                 | 492 us: 1.04x slower                                  |
| coroutines               | 17.8 ms                                                | 18.5 ms: 1.04x slower                                 |
| pickle                   | 7.15 us                                                | 7.49 us: 1.05x slower                                 |
| docutils                 | 1.47 sec                                               | 1.54 sec: 1.05x slower                                |
| scimark_sor              | 82.6 ms                                                | 86.9 ms: 1.05x slower                                 |
| mdp                      | 1.55 sec                                               | 1.64 sec: 1.06x slower                                |
| pprint_pformat           | 954 ms                                                 | 1.01 sec: 1.06x slower                                |
| pyflate                  | 310 ms                                                 | 330 ms: 1.06x slower                                  |
| pprint_safe_repr         | 466 ms                                                 | 498 ms: 1.07x slower                                  |
| json                     | 2.78 ms                                                | 2.97 ms: 1.07x slower                                 |
| raytrace                 | 207 ms                                                 | 222 ms: 1.07x slower                                  |
| xml_etree_iterparse      | 70.1 ms                                                | 75.7 ms: 1.08x slower                                 |
| float                    | 53.0 ms                                                | 57.3 ms: 1.08x slower                                 |
| sqlglot_normalize        | 171 ms                                                 | 185 ms: 1.09x slower                                  |
| nbody                    | 65.6 ms                                                | 71.5 ms: 1.09x slower                                 |
| deepcopy_reduce          | 1.91 us                                                | 2.09 us: 1.09x slower                                 |
| json_loads               | 16.1 us                                                | 17.7 us: 1.10x slower                                 |
| sqlglot_optimize         | 31.1 ms                                                | 34.4 ms: 1.11x slower                                 |
| scimark_monte_carlo      | 46.5 ms                                                | 51.4 ms: 1.11x slower                                 |
| telco                    | 3.41 ms                                                | 3.81 ms: 1.12x slower                                 |
| xml_etree_process        | 35.1 ms                                                | 39.2 ms: 1.12x slower                                 |
| xml_etree_generate       | 48.3 ms                                                | 56.6 ms: 1.17x slower                                 |
| unpickle_list            | 2.65 us                                                | 3.14 us: 1.18x slower                                 |
| pathlib                  | 27.2 ms                                                | 33.1 ms: 1.22x slower                                 |
| sqlite_synth             | 1.27 us                                                | 1.61 us: 1.26x slower                                 |
| mypy2                    | 195 ms                                                 | 259 ms: 1.33x slower                                  |
| async_generators         | 196 ms                                                 | 313 ms: 1.60x slower                                  |
| Geometric mean           | (ref)                                                  | 1.01x faster                                          |

Benchmark hidden because not significant (4): scimark_sparse_mat_mult, crypto_pyaes, async_tree_cpu_io_mixed, tornado_http
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
