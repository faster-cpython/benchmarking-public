# Results vs. base

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 47eb1b5
- commit date: 2024-11-13
- overall geometric mean: 1.044x faster
- HPT reliability: 96.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 260 ms: 1.02x slower                                                       |
| docutils       | 2.69 sec                                                               | 2.61 sec: 1.03x faster                                                     |
| sphinx         | 1.05 sec                                                               | 1.00 sec: 1.05x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 979 ms                                                                 | 619 ms: 1.58x faster                                                       |
| async_tree_io              | 851 ms                                                                 | 596 ms: 1.43x faster                                                       |
| async_tree_memoization     | 415 ms                                                                 | 345 ms: 1.21x faster                                                       |
| async_tree_none            | 330 ms                                                                 | 278 ms: 1.19x faster                                                       |
| async_tree_none_tg         | 324 ms                                                                 | 276 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 578 ms                                                                 | 504 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                 | 493 ms: 1.14x faster                                                       |
| async_tree_memoization_tg  | 378 ms                                                                 | 337 ms: 1.12x faster                                                       |
| coroutines                 | 23.1 ms                                                                | 23.2 ms: 1.01x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.17x faster                                                               |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 94.7 ms                                                                | 98.4 ms: 1.04x slower                                                      |
| float          | 79.6 ms                                                                | 83.9 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.82 ms                                                                | 3.65 ms: 1.05x faster                                                      |
| regex_dna      | 224 ms                                                                 | 217 ms: 1.03x faster                                                       |
| regex_compile  | 130 ms                                                                 | 129 ms: 1.01x faster                                                       |
| regex_v8       | 25.0 ms                                                                | 24.9 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.09 sec                                                               | 2.04 sec: 1.02x faster                                                     |
| json_loads           | 26.4 us                                                                | 26.1 us: 1.01x faster                                                      |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                       |
| pickle_pure_python   | 324 us                                                                 | 328 us: 1.01x slower                                                       |
| xml_etree_generate   | 85.5 ms                                                                | 87.2 ms: 1.02x slower                                                      |
| xml_etree_process    | 59.2 ms                                                                | 61.2 ms: 1.03x slower                                                      |
| xml_etree_parse      | 159 ms                                                                 | 172 ms: 1.08x slower                                                       |
| xml_etree_iterparse  | 105 ms                                                                 | 120 ms: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.03x slower                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.06 ms                                                                | 6.79 ms: 1.04x faster                                                      |
| python_startup         | 12.7 ms                                                                | 12.4 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                                | 22.1 ms: 1.04x faster                                                      |
| django_template | 34.8 ms                                                                | 34.5 ms: 1.01x faster                                                      |
| mako            | 11.7 ms                                                                | 11.7 ms: 1.00x slower                                                      |
| genshi_xml      | 50.5 ms                                                                | 51.6 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 4.72 ms                                                                | 1.74 ms: 2.70x faster                                                      |
| create_gc_cycles           | 2.70 ms                                                                | 1.64 ms: 1.65x faster                                                      |
| k_core                     | 3.62 sec                                                               | 2.20 sec: 1.64x faster                                                     |
| async_tree_io_tg           | 979 ms                                                                 | 619 ms: 1.58x faster                                                       |
| async_tree_io              | 851 ms                                                                 | 596 ms: 1.43x faster                                                       |
| pylint                     | 317 ms                                                                 | 262 ms: 1.21x faster                                                       |
| async_tree_memoization     | 415 ms                                                                 | 345 ms: 1.21x faster                                                       |
| async_tree_none            | 330 ms                                                                 | 278 ms: 1.19x faster                                                       |
| async_tree_none_tg         | 324 ms                                                                 | 276 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 578 ms                                                                 | 504 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                 | 493 ms: 1.14x faster                                                       |
| async_tree_memoization_tg  | 378 ms                                                                 | 337 ms: 1.12x faster                                                       |
| sphinx                     | 1.05 sec                                                               | 1.00 sec: 1.05x faster                                                     |
| regex_effbot               | 3.82 ms                                                                | 3.65 ms: 1.05x faster                                                      |
| pycparser                  | 1.17 sec                                                               | 1.12 sec: 1.05x faster                                                     |
| generators                 | 28.0 ms                                                                | 26.7 ms: 1.05x faster                                                      |
| python_startup_no_site     | 7.06 ms                                                                | 6.79 ms: 1.04x faster                                                      |
| scimark_sor                | 132 ms                                                                 | 127 ms: 1.04x faster                                                       |
| genshi_text                | 22.9 ms                                                                | 22.1 ms: 1.04x faster                                                      |
| docutils                   | 2.69 sec                                                               | 2.61 sec: 1.03x faster                                                     |
| regex_dna                  | 224 ms                                                                 | 217 ms: 1.03x faster                                                       |
| hexiom                     | 6.32 ms                                                                | 6.17 ms: 1.03x faster                                                      |
| tomli_loads                | 2.09 sec                                                               | 2.04 sec: 1.02x faster                                                     |
| python_startup             | 12.7 ms                                                                | 12.4 ms: 1.02x faster                                                      |
| telco                      | 7.84 ms                                                                | 7.70 ms: 1.02x faster                                                      |
| sqlite_synth               | 2.88 us                                                                | 2.82 us: 1.02x faster                                                      |
| scimark_lu                 | 117 ms                                                                 | 115 ms: 1.02x faster                                                       |
| spectral_norm              | 116 ms                                                                 | 115 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.96 ms                                                                | 4.89 ms: 1.02x faster                                                      |
| json_loads                 | 26.4 us                                                                | 26.1 us: 1.01x faster                                                      |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                                       |
| regex_compile              | 130 ms                                                                 | 129 ms: 1.01x faster                                                       |
| logging_format             | 6.17 us                                                                | 6.10 us: 1.01x faster                                                      |
| django_template            | 34.8 ms                                                                | 34.5 ms: 1.01x faster                                                      |
| logging_simple             | 5.60 us                                                                | 5.56 us: 1.01x faster                                                      |
| raytrace                   | 275 ms                                                                 | 273 ms: 1.01x faster                                                       |
| meteor_contest             | 107 ms                                                                 | 106 ms: 1.01x faster                                                       |
| regex_v8                   | 25.0 ms                                                                | 24.9 ms: 1.00x faster                                                      |
| pprint_pformat             | 1.49 sec                                                               | 1.48 sec: 1.00x faster                                                     |
| dulwich_log                | 64.5 ms                                                                | 64.4 ms: 1.00x faster                                                      |
| bench_thread_pool          | 850 us                                                                 | 851 us: 1.00x slower                                                       |
| mako                       | 11.7 ms                                                                | 11.7 ms: 1.00x slower                                                      |
| richards                   | 45.6 ms                                                                | 45.8 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 726 ms                                                                 | 730 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 68.6 ms                                                                | 69.0 ms: 1.01x slower                                                      |
| comprehensions             | 17.0 us                                                                | 17.1 us: 1.01x slower                                                      |
| sympy_str                  | 269 ms                                                                 | 271 ms: 1.01x slower                                                       |
| deepcopy                   | 263 us                                                                 | 264 us: 1.01x slower                                                       |
| richards_super             | 51.8 ms                                                                | 52.2 ms: 1.01x slower                                                      |
| coroutines                 | 23.1 ms                                                                | 23.2 ms: 1.01x slower                                                      |
| go                         | 121 ms                                                                 | 122 ms: 1.01x slower                                                       |
| pickle_pure_python         | 324 us                                                                 | 328 us: 1.01x slower                                                       |
| bpe_tokeniser              | 4.82 sec                                                               | 4.88 sec: 1.01x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                                | 54.4 ms: 1.01x slower                                                      |
| 2to3                       | 256 ms                                                                 | 260 ms: 1.02x slower                                                       |
| deltablue                  | 3.34 ms                                                                | 3.40 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 107 ms                                                                 | 109 ms: 1.02x slower                                                       |
| nqueens                    | 80.7 ms                                                                | 82.1 ms: 1.02x slower                                                      |
| pyflate                    | 470 ms                                                                 | 479 ms: 1.02x slower                                                       |
| xml_etree_generate         | 85.5 ms                                                                | 87.2 ms: 1.02x slower                                                      |
| genshi_xml                 | 50.5 ms                                                                | 51.6 ms: 1.02x slower                                                      |
| sqlglot_transpile          | 1.59 ms                                                                | 1.63 ms: 1.02x slower                                                      |
| mdp                        | 2.65 sec                                                               | 2.72 sec: 1.03x slower                                                     |
| xml_etree_process          | 59.2 ms                                                                | 61.2 ms: 1.03x slower                                                      |
| sqlglot_parse              | 1.29 ms                                                                | 1.33 ms: 1.03x slower                                                      |
| nbody                      | 94.7 ms                                                                | 98.4 ms: 1.04x slower                                                      |
| float                      | 79.6 ms                                                                | 83.9 ms: 1.05x slower                                                      |
| bench_mp_pool              | 79.0 ms                                                                | 84.3 ms: 1.07x slower                                                      |
| xml_etree_parse            | 159 ms                                                                 | 172 ms: 1.08x slower                                                       |
| xml_etree_iterparse        | 105 ms                                                                 | 120 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (24): json, connected_components, sympy_expand, logging_silent, typing_runtime_protocols, shortest_path, coverage, sqlalchemy_imperative, fannkuch, sympy_integrate, sqlalchemy_declarative, json_dumps, sympy_sum, thrift, deepcopy_reduce, pidigits, chaos, async_generators, scimark_fft, crypto_pyaes, pathlib, html5lib, asyncio_websockets, deepcopy_memo

- Geometric mean (including insignificant results): 1.044x faster
# HPT report

- Reliability score: 96.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x