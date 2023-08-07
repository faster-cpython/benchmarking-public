
# Results vs. 3.11.0

- fork: brandtbucher
- ref: uops_enabled
- machine: darwin-arm64
- commit hash: 9016d52
- commit date: 2023-08-06
- overall geometric mean: 1.07x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.59 sec: 1.08x slower                                              |
| Geometric mean | (ref)                                                  | 1.06x slower                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                                |
| nbody          | 65.6 ms                                                | 77.5 ms: 1.18x slower                                               |
| float          | 53.0 ms                                                | 63.7 ms: 1.20x slower                                               |
| Geometric mean | (ref)                                                  | 1.13x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                               |
| regex_dna      | 152 ms                                                 | 151 ms: 1.01x faster                                                |
| regex_v8       | 16.1 ms                                                | 16.0 ms: 1.01x faster                                               |
| regex_compile  | 76.7 ms                                                | 88.7 ms: 1.16x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.76 ms: 1.13x faster                                               |
| unpickle             | 9.67 us                                                | 9.28 us: 1.04x faster                                               |
| pickle_dict          | 18.0 us                                                | 17.9 us: 1.01x faster                                               |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                                |
| pickle_pure_python   | 201 us                                                 | 206 us: 1.03x slower                                                |
| pickle               | 7.15 us                                                | 7.42 us: 1.04x slower                                               |
| pickle_list          | 2.81 us                                                | 2.94 us: 1.05x slower                                               |
| json_loads           | 16.1 us                                                | 17.5 us: 1.08x slower                                               |
| unpickle_pure_python | 159 us                                                 | 173 us: 1.09x slower                                                |
| xml_etree_iterparse  | 70.1 ms                                                | 78.9 ms: 1.13x slower                                               |
| unpickle_list        | 2.65 us                                                | 3.18 us: 1.20x slower                                               |
| xml_etree_process    | 35.1 ms                                                | 42.3 ms: 1.21x slower                                               |
| tomli_loads          | 1.47 sec                                               | 1.84 sec: 1.25x slower                                              |
| xml_etree_generate   | 48.3 ms                                                | 62.0 ms: 1.29x slower                                               |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.18 ms: 1.11x faster                                               |
| python_startup         | 12.4 ms                                                | 11.2 ms: 1.10x faster                                               |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 8.53 ms                                                | 8.68 ms: 1.02x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 99.1 us: 3.39x faster                                               |
| asyncio_tcp              | 651 ms                                                 | 441 ms: 1.48x faster                                                |
| unpack_sequence          | 34.1 ns                                                | 27.9 ns: 1.22x faster                                               |
| coverage                 | 58.4 ms                                                | 50.9 ms: 1.15x faster                                               |
| json_dumps               | 7.63 ms                                                | 6.76 ms: 1.13x faster                                               |
| python_startup_no_site   | 10.2 ms                                                | 9.18 ms: 1.11x faster                                               |
| python_startup           | 12.4 ms                                                | 11.2 ms: 1.10x faster                                               |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.36 sec: 1.06x faster                                              |
| unpickle                 | 9.67 us                                                | 9.28 us: 1.04x faster                                               |
| regex_effbot             | 2.63 ms                                                | 2.56 ms: 1.03x faster                                               |
| chaos                    | 49.4 ms                                                | 48.1 ms: 1.03x faster                                               |
| async_tree_io            | 704 ms                                                 | 686 ms: 1.03x faster                                                |
| crypto_pyaes             | 51.7 ms                                                | 50.4 ms: 1.03x faster                                               |
| async_tree_none          | 286 ms                                                 | 278 ms: 1.03x faster                                                |
| create_gc_cycles         | 716 us                                                 | 703 us: 1.02x faster                                                |
| sqlglot_parse            | 959 us                                                 | 947 us: 1.01x faster                                                |
| regex_dna                | 152 ms                                                 | 151 ms: 1.01x faster                                                |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                               |
| regex_v8                 | 16.1 ms                                                | 16.0 ms: 1.01x faster                                               |
| pickle_dict              | 18.0 us                                                | 17.9 us: 1.01x faster                                               |
| generators               | 28.8 ms                                                | 28.7 ms: 1.00x faster                                               |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                                |
| sqlglot_transpile        | 1.12 ms                                                | 1.14 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 541 ms: 1.01x slower                                                |
| mako                     | 8.53 ms                                                | 8.68 ms: 1.02x slower                                               |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.03x slower                                                |
| pickle_pure_python       | 201 us                                                 | 206 us: 1.03x slower                                                |
| pickle                   | 7.15 us                                                | 7.42 us: 1.04x slower                                               |
| bench_mp_pool            | 43.9 ms                                                | 45.7 ms: 1.04x slower                                               |
| pycparser                | 698 ms                                                 | 730 ms: 1.05x slower                                                |
| pickle_list              | 2.81 us                                                | 2.94 us: 1.05x slower                                               |
| dulwich_log              | 30.3 ms                                                | 31.8 ms: 1.05x slower                                               |
| pathlib                  | 27.2 ms                                                | 28.7 ms: 1.05x slower                                               |
| deltablue                | 2.81 ms                                                | 3.00 ms: 1.07x slower                                               |
| deepcopy                 | 223 us                                                 | 238 us: 1.07x slower                                                |
| richards_super           | 39.2 ms                                                | 42.0 ms: 1.07x slower                                               |
| spectral_norm            | 72.6 ms                                                | 78.2 ms: 1.08x slower                                               |
| docutils                 | 1.47 sec                                               | 1.59 sec: 1.08x slower                                              |
| json                     | 2.78 ms                                                | 3.00 ms: 1.08x slower                                               |
| json_loads               | 16.1 us                                                | 17.5 us: 1.08x slower                                               |
| unpickle_pure_python     | 159 us                                                 | 173 us: 1.09x slower                                                |
| logging_simple           | 3.55 us                                                | 3.91 us: 1.10x slower                                               |
| logging_format           | 3.78 us                                                | 4.18 us: 1.10x slower                                               |
| deepcopy_reduce          | 1.91 us                                                | 2.12 us: 1.11x slower                                               |
| bench_thread_pool        | 474 us                                                 | 527 us: 1.11x slower                                                |
| scimark_fft              | 200 ms                                                 | 222 ms: 1.11x slower                                                |
| scimark_lu               | 73.3 ms                                                | 81.6 ms: 1.11x slower                                               |
| deepcopy_memo            | 26.3 us                                                | 29.4 us: 1.12x slower                                               |
| xml_etree_iterparse      | 70.1 ms                                                | 78.9 ms: 1.13x slower                                               |
| meteor_contest           | 73.5 ms                                                | 82.9 ms: 1.13x slower                                               |
| mdp                      | 1.55 sec                                               | 1.75 sec: 1.13x slower                                              |
| pprint_safe_repr         | 466 ms                                                 | 533 ms: 1.14x slower                                                |
| raytrace                 | 207 ms                                                 | 237 ms: 1.14x slower                                                |
| pprint_pformat           | 954 ms                                                 | 1.09 sec: 1.14x slower                                              |
| logging_silent           | 68.1 ns                                                | 78.2 ns: 1.15x slower                                               |
| regex_compile            | 76.7 ms                                                | 88.7 ms: 1.16x slower                                               |
| coroutines               | 17.8 ms                                                | 20.6 ms: 1.16x slower                                               |
| go                       | 109 ms                                                 | 127 ms: 1.17x slower                                                |
| scimark_monte_carlo      | 46.5 ms                                                | 54.6 ms: 1.17x slower                                               |
| sqlglot_normalize        | 171 ms                                                 | 201 ms: 1.18x slower                                                |
| nbody                    | 65.6 ms                                                | 77.5 ms: 1.18x slower                                               |
| sqlglot_optimize         | 31.1 ms                                                | 36.9 ms: 1.19x slower                                               |
| richards                 | 32.2 ms                                                | 38.3 ms: 1.19x slower                                               |
| unpickle_list            | 2.65 us                                                | 3.18 us: 1.20x slower                                               |
| float                    | 53.0 ms                                                | 63.7 ms: 1.20x slower                                               |
| xml_etree_process        | 35.1 ms                                                | 42.3 ms: 1.21x slower                                               |
| comprehensions           | 16.1 us                                                | 19.4 us: 1.21x slower                                               |
| nqueens                  | 59.8 ms                                                | 73.0 ms: 1.22x slower                                               |
| pyflate                  | 310 ms                                                 | 387 ms: 1.25x slower                                                |
| tomli_loads              | 1.47 sec                                               | 1.84 sec: 1.25x slower                                              |
| xml_etree_generate       | 48.3 ms                                                | 62.0 ms: 1.29x slower                                               |
| sqlite_synth             | 1.27 us                                                | 1.64 us: 1.29x slower                                               |
| hexiom                   | 4.72 ms                                                | 6.15 ms: 1.30x slower                                               |
| fannkuch                 | 261 ms                                                 | 341 ms: 1.31x slower                                                |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 4.24 ms: 1.33x slower                                               |
| telco                    | 3.41 ms                                                | 4.60 ms: 1.35x slower                                               |
| mypy2                    | 195 ms                                                 | 268 ms: 1.37x slower                                                |
| scimark_sor              | 82.6 ms                                                | 121 ms: 1.46x slower                                                |
| async_generators         | 196 ms                                                 | 323 ms: 1.64x slower                                                |
| Geometric mean           | (ref)                                                  | 1.07x slower                                                        |

Benchmark hidden because not significant (2): async_tree_memoization, tornado_http
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230806-3.13.0a0-9016d52/bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52.json: dask
