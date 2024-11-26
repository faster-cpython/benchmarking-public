# Results vs. base

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: fb5fdad
- commit date: 2024-11-10
- overall geometric mean: 1.047x faster
- HPT reliability: 94.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 258 ms: 1.01x slower                                                       |
| docutils       | 2.69 sec                                                               | 2.62 sec: 1.03x faster                                                     |
| html5lib       | 65.2 ms                                                                | 64.4 ms: 1.01x faster                                                      |
| sphinx         | 1.05 sec                                                               | 1.01 sec: 1.05x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 979 ms                                                                 | 637 ms: 1.54x faster                                                       |
| async_tree_io              | 851 ms                                                                 | 627 ms: 1.36x faster                                                       |
| async_tree_none_tg         | 324 ms                                                                 | 247 ms: 1.31x faster                                                       |
| async_tree_none            | 330 ms                                                                 | 259 ms: 1.27x faster                                                       |
| async_tree_memoization     | 415 ms                                                                 | 337 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                 | 466 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 578 ms                                                                 | 488 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 378 ms                                                                 | 320 ms: 1.18x faster                                                       |
| async_generators           | 430 ms                                                                 | 429 ms: 1.00x faster                                                       |
| coroutines                 | 23.1 ms                                                                | 23.6 ms: 1.03x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.19x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.6 ms                                                                | 78.8 ms: 1.01x faster                                                      |
| pidigits       | 187 ms                                                                 | 188 ms: 1.00x slower                                                       |
| nbody          | 94.7 ms                                                                | 96.3 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.82 ms                                                                | 3.72 ms: 1.03x faster                                                      |
| regex_v8       | 25.0 ms                                                                | 24.7 ms: 1.01x faster                                                      |
| regex_dna      | 224 ms                                                                 | 222 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                                 | 144 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 105 ms                                                                 | 99.9 ms: 1.05x faster                                                      |
| xml_etree_generate   | 85.5 ms                                                                | 84.8 ms: 1.01x faster                                                      |
| unpickle_pure_python | 219 us                                                                 | 218 us: 1.01x faster                                                       |
| tomli_loads          | 2.09 sec                                                               | 2.08 sec: 1.01x faster                                                     |
| json_loads           | 26.4 us                                                                | 26.7 us: 1.01x slower                                                      |
| pickle_pure_python   | 324 us                                                                 | 330 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.06 ms                                                                | 6.83 ms: 1.03x faster                                                      |
| python_startup         | 12.7 ms                                                                | 12.4 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                                | 22.3 ms: 1.03x faster                                                      |
| mako            | 11.7 ms                                                                | 11.5 ms: 1.01x faster                                                      |
| django_template | 34.8 ms                                                                | 35.0 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 4.72 ms                                                                | 1.89 ms: 2.49x faster                                                      |
| k_core                     | 3.62 sec                                                               | 2.29 sec: 1.58x faster                                                     |
| async_tree_io_tg           | 979 ms                                                                 | 637 ms: 1.54x faster                                                       |
| create_gc_cycles           | 2.70 ms                                                                | 1.77 ms: 1.53x faster                                                      |
| async_tree_io              | 851 ms                                                                 | 627 ms: 1.36x faster                                                       |
| async_tree_none_tg         | 324 ms                                                                 | 247 ms: 1.31x faster                                                       |
| async_tree_none            | 330 ms                                                                 | 259 ms: 1.27x faster                                                       |
| async_tree_memoization     | 415 ms                                                                 | 337 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                 | 466 ms: 1.21x faster                                                       |
| pylint                     | 317 ms                                                                 | 263 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 578 ms                                                                 | 488 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 378 ms                                                                 | 320 ms: 1.18x faster                                                       |
| xml_etree_parse            | 159 ms                                                                 | 144 ms: 1.10x faster                                                       |
| bpe_tokeniser              | 4.82 sec                                                               | 4.58 sec: 1.05x faster                                                     |
| xml_etree_iterparse        | 105 ms                                                                 | 99.9 ms: 1.05x faster                                                      |
| sphinx                     | 1.05 sec                                                               | 1.01 sec: 1.05x faster                                                     |
| mdp                        | 2.65 sec                                                               | 2.54 sec: 1.05x faster                                                     |
| python_startup_no_site     | 7.06 ms                                                                | 6.83 ms: 1.03x faster                                                      |
| regex_effbot               | 3.82 ms                                                                | 3.72 ms: 1.03x faster                                                      |
| docutils                   | 2.69 sec                                                               | 2.62 sec: 1.03x faster                                                     |
| genshi_text                | 22.9 ms                                                                | 22.3 ms: 1.03x faster                                                      |
| python_startup             | 12.7 ms                                                                | 12.4 ms: 1.02x faster                                                      |
| generators                 | 28.0 ms                                                                | 27.4 ms: 1.02x faster                                                      |
| sqlalchemy_imperative      | 16.9 ms                                                                | 16.6 ms: 1.02x faster                                                      |
| mako                       | 11.7 ms                                                                | 11.5 ms: 1.01x faster                                                      |
| scimark_lu                 | 117 ms                                                                 | 115 ms: 1.01x faster                                                       |
| scimark_fft                | 369 ms                                                                 | 364 ms: 1.01x faster                                                       |
| deepcopy_reduce            | 2.74 us                                                                | 2.70 us: 1.01x faster                                                      |
| regex_v8                   | 25.0 ms                                                                | 24.7 ms: 1.01x faster                                                      |
| html5lib                   | 65.2 ms                                                                | 64.4 ms: 1.01x faster                                                      |
| fannkuch                   | 410 ms                                                                 | 405 ms: 1.01x faster                                                       |
| telco                      | 7.84 ms                                                                | 7.75 ms: 1.01x faster                                                      |
| pycparser                  | 1.17 sec                                                               | 1.16 sec: 1.01x faster                                                     |
| thrift                     | 782 us                                                                 | 774 us: 1.01x faster                                                       |
| float                      | 79.6 ms                                                                | 78.8 ms: 1.01x faster                                                      |
| regex_dna                  | 224 ms                                                                 | 222 ms: 1.01x faster                                                       |
| sqlite_synth               | 2.88 us                                                                | 2.85 us: 1.01x faster                                                      |
| xml_etree_generate         | 85.5 ms                                                                | 84.8 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 219 us                                                                 | 218 us: 1.01x faster                                                       |
| tomli_loads                | 2.09 sec                                                               | 2.08 sec: 1.01x faster                                                     |
| async_generators           | 430 ms                                                                 | 429 ms: 1.00x faster                                                       |
| sqlalchemy_declarative     | 128 ms                                                                 | 127 ms: 1.00x faster                                                       |
| spectral_norm              | 116 ms                                                                 | 117 ms: 1.00x slower                                                       |
| sympy_integrate            | 19.9 ms                                                                | 19.9 ms: 1.00x slower                                                      |
| pidigits                   | 187 ms                                                                 | 188 ms: 1.00x slower                                                       |
| deepcopy_memo              | 30.4 us                                                                | 30.6 us: 1.01x slower                                                      |
| chaos                      | 61.1 ms                                                                | 61.5 ms: 1.01x slower                                                      |
| django_template            | 34.8 ms                                                                | 35.0 ms: 1.01x slower                                                      |
| bench_thread_pool          | 850 us                                                                 | 856 us: 1.01x slower                                                       |
| pprint_pformat             | 1.49 sec                                                               | 1.50 sec: 1.01x slower                                                     |
| go                         | 121 ms                                                                 | 122 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 107 ms                                                                 | 108 ms: 1.01x slower                                                       |
| 2to3                       | 256 ms                                                                 | 258 ms: 1.01x slower                                                       |
| deltablue                  | 3.34 ms                                                                | 3.37 ms: 1.01x slower                                                      |
| meteor_contest             | 107 ms                                                                 | 108 ms: 1.01x slower                                                       |
| json_loads                 | 26.4 us                                                                | 26.7 us: 1.01x slower                                                      |
| dulwich_log                | 64.5 ms                                                                | 65.3 ms: 1.01x slower                                                      |
| hexiom                     | 6.32 ms                                                                | 6.40 ms: 1.01x slower                                                      |
| json                       | 4.88 ms                                                                | 4.95 ms: 1.01x slower                                                      |
| raytrace                   | 275 ms                                                                 | 278 ms: 1.01x slower                                                       |
| sympy_str                  | 269 ms                                                                 | 273 ms: 1.01x slower                                                       |
| scimark_sor                | 132 ms                                                                 | 134 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.29 ms                                                                | 1.31 ms: 1.02x slower                                                      |
| coverage                   | 84.1 ms                                                                | 85.4 ms: 1.02x slower                                                      |
| pprint_safe_repr           | 726 ms                                                                 | 738 ms: 1.02x slower                                                       |
| nbody                      | 94.7 ms                                                                | 96.3 ms: 1.02x slower                                                      |
| scimark_monte_carlo        | 68.6 ms                                                                | 69.9 ms: 1.02x slower                                                      |
| pickle_pure_python         | 324 us                                                                 | 330 us: 1.02x slower                                                       |
| sqlglot_transpile          | 1.59 ms                                                                | 1.63 ms: 1.02x slower                                                      |
| richards                   | 45.6 ms                                                                | 46.6 ms: 1.02x slower                                                      |
| richards_super             | 51.8 ms                                                                | 53.0 ms: 1.02x slower                                                      |
| coroutines                 | 23.1 ms                                                                | 23.6 ms: 1.03x slower                                                      |
| nqueens                    | 80.7 ms                                                                | 82.9 ms: 1.03x slower                                                      |
| bench_mp_pool              | 79.0 ms                                                                | 82.2 ms: 1.04x slower                                                      |
| logging_silent             | 105 ns                                                                 | 110 ns: 1.05x slower                                                       |
| crypto_pyaes               | 71.7 ms                                                                | 75.4 ms: 1.05x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (18): logging_format, logging_simple, genshi_xml, connected_components, deepcopy, comprehensions, xml_etree_process, regex_compile, sqlglot_optimize, asyncio_websockets, shortest_path, sympy_sum, pyflate, typing_runtime_protocols, pathlib, json_dumps, scimark_sparse_mat_mult, sympy_expand

- Geometric mean (including insignificant results): 1.047x faster
# HPT report

- Reliability score: 94.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x