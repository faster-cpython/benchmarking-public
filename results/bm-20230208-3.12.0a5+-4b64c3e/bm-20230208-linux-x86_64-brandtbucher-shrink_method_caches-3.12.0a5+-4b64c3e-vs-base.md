
# Results vs. base

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 4b64c3e
- commit date: 2023-02-08
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230209-linux-x86_64-python-f1f3af7b8245e61a2e0a-3.12.0a5+-f1f3af7 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.00x slower                                                         |
| chameleon      | 6.40 ms                                                                | 6.36 ms: 1.01x faster                                                        |
| docutils       | 2.53 sec                                                               | 2.54 sec: 1.00x slower                                                       |
| tornado_http   | 93.8 ms                                                                | 94.8 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230209-linux-x86_64-python-f1f3af7b8245e61a2e0a-3.12.0a5+-f1f3af7 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 94.4 ms                                                                | 93.1 ms: 1.01x faster                                                        |
| pidigits       | 193 ms                                                                 | 192 ms: 1.00x faster                                                         |
| float          | 72.5 ms                                                                | 73.0 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230209-linux-x86_64-python-f1f3af7b8245e61a2e0a-3.12.0a5+-f1f3af7 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                         |
| regex_dna      | 211 ms                                                                 | 218 ms: 1.03x slower                                                         |
| regex_v8       | 21.3 ms                                                                | 22.0 ms: 1.04x slower                                                        |
| regex_effbot   | 3.39 ms                                                                | 3.52 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230209-linux-x86_64-python-f1f3af7b8245e61a2e0a-3.12.0a5+-f1f3af7 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_list          | 4.19 us                                                                | 4.13 us: 1.01x faster                                                        |
| pickle_dict          | 30.6 us                                                                | 30.4 us: 1.01x faster                                                        |
| unpickle_list        | 4.96 us                                                                | 4.98 us: 1.00x slower                                                        |
| xml_etree_process    | 55.0 ms                                                                | 55.3 ms: 1.01x slower                                                        |
| unpickle_pure_python | 198 us                                                                 | 199 us: 1.01x slower                                                         |
| xml_etree_generate   | 79.9 ms                                                                | 80.5 ms: 1.01x slower                                                        |
| json_loads           | 23.7 us                                                                | 23.9 us: 1.01x slower                                                        |
| pickle_pure_python   | 285 us                                                                 | 294 us: 1.03x slower                                                         |
| unpickle             | 13.0 us                                                                | 13.7 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (4): json_dumps, xml_etree_parse, xml_etree_iterparse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230209-linux-x86_64-python-f1f3af7b8245e61a2e0a-3.12.0a5+-f1f3af7 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.50 ms                                                                | 6.42 ms: 1.01x faster                                                        |
| python_startup         | 8.96 ms                                                                | 8.86 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230209-linux-x86_64-python-f1f3af7b8245e61a2e0a-3.12.0a5+-f1f3af7 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 33.0 ms                                                                | 32.6 ms: 1.01x faster                                                        |
| genshi_text     | 21.0 ms                                                                | 20.8 ms: 1.01x faster                                                        |
| mako            | 9.80 ms                                                                | 9.90 ms: 1.01x slower                                                        |
| genshi_xml      | 46.2 ms                                                                | 47.0 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20230209-linux-x86_64-python-f1f3af7b8245e61a2e0a-3.12.0a5+-f1f3af7 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal            | 3.91 ms                                                                | 3.65 ms: 1.07x faster                                                        |
| coroutines              | 25.7 ms                                                                | 24.5 ms: 1.05x faster                                                        |
| spectral_norm           | 96.7 ms                                                                | 93.4 ms: 1.03x faster                                                        |
| async_tree_memoization  | 664 ms                                                                 | 645 ms: 1.03x faster                                                         |
| nqueens                 | 78.1 ms                                                                | 76.2 ms: 1.02x faster                                                        |
| fannkuch                | 369 ms                                                                 | 361 ms: 1.02x faster                                                         |
| create_gc_cycles        | 1.49 ms                                                                | 1.46 ms: 1.02x faster                                                        |
| meteor_contest          | 105 ms                                                                 | 103 ms: 1.02x faster                                                         |
| nbody                   | 94.4 ms                                                                | 93.1 ms: 1.01x faster                                                        |
| pickle_list             | 4.19 us                                                                | 4.13 us: 1.01x faster                                                        |
| django_template         | 33.0 ms                                                                | 32.6 ms: 1.01x faster                                                        |
| python_startup_no_site  | 6.50 ms                                                                | 6.42 ms: 1.01x faster                                                        |
| python_startup          | 8.96 ms                                                                | 8.86 ms: 1.01x faster                                                        |
| pickle_dict             | 30.6 us                                                                | 30.4 us: 1.01x faster                                                        |
| genshi_text             | 21.0 ms                                                                | 20.8 ms: 1.01x faster                                                        |
| chameleon               | 6.40 ms                                                                | 6.36 ms: 1.01x faster                                                        |
| pidigits                | 193 ms                                                                 | 192 ms: 1.00x faster                                                         |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.00x slower                                                         |
| unpickle_list           | 4.96 us                                                                | 4.98 us: 1.00x slower                                                        |
| docutils                | 2.53 sec                                                               | 2.54 sec: 1.00x slower                                                       |
| xml_etree_process       | 55.0 ms                                                                | 55.3 ms: 1.01x slower                                                        |
| unpickle_pure_python    | 198 us                                                                 | 199 us: 1.01x slower                                                         |
| float                   | 72.5 ms                                                                | 73.0 ms: 1.01x slower                                                        |
| xml_etree_generate      | 79.9 ms                                                                | 80.5 ms: 1.01x slower                                                        |
| deepcopy                | 329 us                                                                 | 331 us: 1.01x slower                                                         |
| scimark_monte_carlo     | 65.6 ms                                                                | 66.1 ms: 1.01x slower                                                        |
| sympy_integrate         | 19.7 ms                                                                | 19.8 ms: 1.01x slower                                                        |
| crypto_pyaes            | 73.0 ms                                                                | 73.6 ms: 1.01x slower                                                        |
| asyncio_tcp             | 501 ms                                                                 | 505 ms: 1.01x slower                                                         |
| sqlite_synth            | 2.57 us                                                                | 2.59 us: 1.01x slower                                                        |
| regex_compile           | 128 ms                                                                 | 129 ms: 1.01x slower                                                         |
| bench_thread_pool       | 783 us                                                                 | 791 us: 1.01x slower                                                         |
| go                      | 132 ms                                                                 | 134 ms: 1.01x slower                                                         |
| tornado_http            | 93.8 ms                                                                | 94.8 ms: 1.01x slower                                                        |
| scimark_fft             | 305 ms                                                                 | 308 ms: 1.01x slower                                                         |
| sympy_str               | 268 ms                                                                 | 271 ms: 1.01x slower                                                         |
| mako                    | 9.80 ms                                                                | 9.90 ms: 1.01x slower                                                        |
| json_loads              | 23.7 us                                                                | 23.9 us: 1.01x slower                                                        |
| sqlalchemy_declarative  | 136 ms                                                                 | 137 ms: 1.01x slower                                                         |
| pycparser               | 1.08 sec                                                               | 1.09 sec: 1.01x slower                                                       |
| gunicorn                | 1.08 ms                                                                | 1.09 ms: 1.01x slower                                                        |
| mypy2                   | 328 ms                                                                 | 331 ms: 1.01x slower                                                         |
| deepcopy_memo           | 34.1 us                                                                | 34.5 us: 1.01x slower                                                        |
| aiohttp                 | 1.00 ms                                                                | 1.02 ms: 1.01x slower                                                        |
| sympy_sum               | 157 ms                                                                 | 158 ms: 1.01x slower                                                         |
| scimark_sor             | 105 ms                                                                 | 107 ms: 1.01x slower                                                         |
| pprint_safe_repr        | 677 ms                                                                 | 686 ms: 1.01x slower                                                         |
| deepcopy_reduce         | 2.86 us                                                                | 2.90 us: 1.01x slower                                                        |
| async_generators        | 429 ms                                                                 | 435 ms: 1.01x slower                                                         |
| genshi_xml              | 46.2 ms                                                                | 47.0 ms: 1.02x slower                                                        |
| pyflate                 | 399 ms                                                                 | 406 ms: 1.02x slower                                                         |
| dulwich_log             | 62.5 ms                                                                | 63.6 ms: 1.02x slower                                                        |
| chaos                   | 65.2 ms                                                                | 66.4 ms: 1.02x slower                                                        |
| deltablue               | 3.14 ms                                                                | 3.19 ms: 1.02x slower                                                        |
| pprint_pformat          | 1.39 sec                                                               | 1.42 sec: 1.02x slower                                                       |
| sqlglot_optimize        | 50.8 ms                                                                | 51.8 ms: 1.02x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                                | 1.74 ms: 1.02x slower                                                        |
| sqlglot_parse           | 1.41 ms                                                                | 1.45 ms: 1.02x slower                                                        |
| raytrace                | 279 ms                                                                 | 286 ms: 1.02x slower                                                         |
| sqlglot_normalize       | 105 ms                                                                 | 108 ms: 1.02x slower                                                         |
| json                    | 4.55 ms                                                                | 4.66 ms: 1.02x slower                                                        |
| generators              | 74.9 ms                                                                | 76.9 ms: 1.03x slower                                                        |
| unpack_sequence         | 43.0 ns                                                                | 44.2 ns: 1.03x slower                                                        |
| richards                | 41.6 ms                                                                | 42.8 ms: 1.03x slower                                                        |
| pickle_pure_python      | 285 us                                                                 | 294 us: 1.03x slower                                                         |
| sqlalchemy_imperative   | 17.9 ms                                                                | 18.4 ms: 1.03x slower                                                        |
| regex_dna               | 211 ms                                                                 | 218 ms: 1.03x slower                                                         |
| regex_v8                | 21.3 ms                                                                | 22.0 ms: 1.04x slower                                                        |
| regex_effbot            | 3.39 ms                                                                | 3.52 ms: 1.04x slower                                                        |
| logging_format          | 6.24 us                                                                | 6.49 us: 1.04x slower                                                        |
| logging_simple          | 5.72 us                                                                | 5.95 us: 1.04x slower                                                        |
| coverage                | 96.4 ms                                                                | 101 ms: 1.05x slower                                                         |
| unpickle                | 13.0 us                                                                | 13.7 us: 1.05x slower                                                        |
| logging_silent          | 90.8 ns                                                                | 95.9 ns: 1.06x slower                                                        |
| scimark_sparse_mat_mult | 4.03 ms                                                                | 4.27 ms: 1.06x slower                                                        |
| mdp                     | 2.51 sec                                                               | 2.70 sec: 1.07x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (16): pathlib, hexiom, sympy_expand, async_tree_cpu_io_mixed, async_tree_io, thrift, telco, json_dumps, bench_mp_pool, async_tree_none, html5lib, xml_etree_parse, xml_etree_iterparse, pickle, djangocms, scimark_lu
