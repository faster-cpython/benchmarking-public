
# Results vs. 3.10.4

- fork: brandtbucher
- ref: uops_enabled
- machine: darwin-arm64
- commit hash: 9016d52
- commit date: 2023-08-06
- overall geometric mean: 1.13x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.59 sec: 1.12x faster                                              |
| tornado_http   | 91.9 ms                                                | 74.0 ms: 1.24x faster                                               |
| Geometric mean | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 77.5 ms: 1.22x faster                                               |
| float          | 72.3 ms                                                | 63.7 ms: 1.14x faster                                               |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 17.5 ms                                                | 16.0 ms: 1.10x faster                                               |
| regex_compile  | 96.6 ms                                                | 88.7 ms: 1.09x faster                                               |
| regex_dna      | 160 ms                                                 | 151 ms: 1.06x faster                                                |
| regex_effbot   | 2.45 ms                                                | 2.56 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 206 us: 1.38x faster                                                |
| json_dumps           | 8.38 ms                                                | 6.76 ms: 1.24x faster                                               |
| unpickle_pure_python | 203 us                                                 | 173 us: 1.18x faster                                                |
| xml_etree_process    | 45.1 ms                                                | 42.3 ms: 1.06x faster                                               |
| unpickle             | 9.77 us                                                | 9.28 us: 1.05x faster                                               |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.00x slower                                               |
| pickle               | 7.36 us                                                | 7.42 us: 1.01x slower                                               |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.03x slower                                                |
| json_loads           | 16.9 us                                                | 17.5 us: 1.03x slower                                               |
| pickle_list          | 2.83 us                                                | 2.94 us: 1.04x slower                                               |
| tomli_loads          | 1.76 sec                                               | 1.84 sec: 1.04x slower                                              |
| xml_etree_iterparse  | 72.6 ms                                                | 78.9 ms: 1.09x slower                                               |
| xml_etree_generate   | 54.3 ms                                                | 62.0 ms: 1.14x slower                                               |
| unpickle_list        | 2.66 us                                                | 3.18 us: 1.19x slower                                               |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.2 ms: 1.12x faster                                               |
| python_startup_no_site | 9.73 ms                                                | 9.18 ms: 1.06x faster                                               |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 10.5 ms                                                | 8.68 ms: 1.21x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 99.1 us: 3.47x faster                                               |
| deltablue                | 5.15 ms                                                | 3.00 ms: 1.72x faster                                               |
| crypto_pyaes             | 78.0 ms                                                | 50.4 ms: 1.55x faster                                               |
| asyncio_tcp              | 673 ms                                                 | 441 ms: 1.52x faster                                                |
| logging_silent           | 119 ns                                                 | 78.2 ns: 1.52x faster                                               |
| async_tree_memoization   | 493 ms                                                 | 329 ms: 1.50x faster                                                |
| async_tree_io            | 1.02 sec                                               | 686 ms: 1.49x faster                                                |
| richards_super           | 60.7 ms                                                | 42.0 ms: 1.44x faster                                               |
| async_tree_none          | 402 ms                                                 | 278 ms: 1.44x faster                                                |
| sqlglot_parse            | 1.33 ms                                                | 947 us: 1.41x faster                                                |
| chaos                    | 66.8 ms                                                | 48.1 ms: 1.39x faster                                               |
| raytrace                 | 328 ms                                                 | 237 ms: 1.39x faster                                                |
| unpack_sequence          | 38.7 ns                                                | 27.9 ns: 1.39x faster                                               |
| pickle_pure_python       | 284 us                                                 | 206 us: 1.38x faster                                                |
| sqlglot_transpile        | 1.54 ms                                                | 1.14 ms: 1.35x faster                                               |
| scimark_lu               | 110 ms                                                 | 81.6 ms: 1.35x faster                                               |
| richards                 | 51.4 ms                                                | 38.3 ms: 1.34x faster                                               |
| scimark_monte_carlo      | 72.2 ms                                                | 54.6 ms: 1.32x faster                                               |
| go                       | 165 ms                                                 | 127 ms: 1.30x faster                                                |
| pycparser                | 915 ms                                                 | 730 ms: 1.25x faster                                                |
| create_gc_cycles         | 876 us                                                 | 703 us: 1.25x faster                                                |
| tornado_http             | 91.9 ms                                                | 74.0 ms: 1.24x faster                                               |
| json_dumps               | 8.38 ms                                                | 6.76 ms: 1.24x faster                                               |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 541 ms: 1.24x faster                                                |
| spectral_norm            | 96.4 ms                                                | 78.2 ms: 1.23x faster                                               |
| nbody                    | 94.1 ms                                                | 77.5 ms: 1.22x faster                                               |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.36 sec: 1.21x faster                                              |
| mako                     | 10.5 ms                                                | 8.68 ms: 1.21x faster                                               |
| logging_format           | 5.01 us                                                | 4.18 us: 1.20x faster                                               |
| logging_simple           | 4.63 us                                                | 3.91 us: 1.18x faster                                               |
| unpickle_pure_python     | 203 us                                                 | 173 us: 1.18x faster                                                |
| deepcopy_memo            | 34.5 us                                                | 29.4 us: 1.17x faster                                               |
| pyflate                  | 453 ms                                                 | 387 ms: 1.17x faster                                                |
| dulwich_log              | 37.1 ms                                                | 31.8 ms: 1.17x faster                                               |
| deepcopy                 | 278 us                                                 | 238 us: 1.17x faster                                                |
| mypy2                    | 308 ms                                                 | 268 ms: 1.15x faster                                                |
| generators               | 32.9 ms                                                | 28.7 ms: 1.15x faster                                               |
| pprint_safe_repr         | 609 ms                                                 | 533 ms: 1.14x faster                                                |
| pprint_pformat           | 1.24 sec                                               | 1.09 sec: 1.14x faster                                              |
| float                    | 72.3 ms                                                | 63.7 ms: 1.14x faster                                               |
| deepcopy_reduce          | 2.38 us                                                | 2.12 us: 1.12x faster                                               |
| docutils                 | 1.78 sec                                               | 1.59 sec: 1.12x faster                                              |
| python_startup           | 12.6 ms                                                | 11.2 ms: 1.12x faster                                               |
| regex_v8                 | 17.5 ms                                                | 16.0 ms: 1.10x faster                                               |
| regex_compile            | 96.6 ms                                                | 88.7 ms: 1.09x faster                                               |
| xml_etree_process        | 45.1 ms                                                | 42.3 ms: 1.06x faster                                               |
| regex_dna                | 160 ms                                                 | 151 ms: 1.06x faster                                                |
| python_startup_no_site   | 9.73 ms                                                | 9.18 ms: 1.06x faster                                               |
| unpickle                 | 9.77 us                                                | 9.28 us: 1.05x faster                                               |
| scimark_sor              | 127 ms                                                 | 121 ms: 1.05x faster                                                |
| scimark_fft              | 232 ms                                                 | 222 ms: 1.05x faster                                                |
| bench_thread_pool        | 548 us                                                 | 527 us: 1.04x faster                                                |
| json                     | 3.10 ms                                                | 3.00 ms: 1.03x faster                                               |
| sqlglot_optimize         | 38.0 ms                                                | 36.9 ms: 1.03x faster                                               |
| hexiom                   | 6.32 ms                                                | 6.15 ms: 1.03x faster                                               |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.00x slower                                               |
| pickle                   | 7.36 us                                                | 7.42 us: 1.01x slower                                               |
| coroutines               | 20.2 ms                                                | 20.6 ms: 1.02x slower                                               |
| sqlglot_normalize        | 197 ms                                                 | 201 ms: 1.02x slower                                                |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.03x slower                                                |
| json_loads               | 16.9 us                                                | 17.5 us: 1.03x slower                                               |
| pickle_list              | 2.83 us                                                | 2.94 us: 1.04x slower                                               |
| tomli_loads              | 1.76 sec                                               | 1.84 sec: 1.04x slower                                              |
| regex_effbot             | 2.45 ms                                                | 2.56 ms: 1.05x slower                                               |
| mdp                      | 1.67 sec                                               | 1.75 sec: 1.05x slower                                              |
| meteor_contest           | 78.6 ms                                                | 82.9 ms: 1.05x slower                                               |
| nqueens                  | 68.1 ms                                                | 73.0 ms: 1.07x slower                                               |
| fannkuch                 | 317 ms                                                 | 341 ms: 1.07x slower                                                |
| xml_etree_iterparse      | 72.6 ms                                                | 78.9 ms: 1.09x slower                                               |
| comprehensions           | 17.7 us                                                | 19.4 us: 1.10x slower                                               |
| sqlite_synth             | 1.47 us                                                | 1.64 us: 1.11x slower                                               |
| bench_mp_pool            | 41.0 ms                                                | 45.7 ms: 1.12x slower                                               |
| xml_etree_generate       | 54.3 ms                                                | 62.0 ms: 1.14x slower                                               |
| unpickle_list            | 2.66 us                                                | 3.18 us: 1.19x slower                                               |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 4.24 ms: 1.22x slower                                               |
| coverage                 | 40.8 ms                                                | 50.9 ms: 1.25x slower                                               |
| telco                    | 3.68 ms                                                | 4.60 ms: 1.25x slower                                               |
| dask                     | 258 ms                                                 | 345 ms: 1.34x slower                                                |
| async_generators         | 233 ms                                                 | 323 ms: 1.38x slower                                                |
| Geometric mean           | (ref)                                                  | 1.13x faster                                                        |

Benchmark hidden because not significant (2): pathlib, gc_traversal
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
