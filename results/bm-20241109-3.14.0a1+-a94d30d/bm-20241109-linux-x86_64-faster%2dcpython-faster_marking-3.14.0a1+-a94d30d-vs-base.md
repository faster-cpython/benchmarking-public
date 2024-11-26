# Results vs. base

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: a94d30d
- commit date: 2024-11-09
- overall geometric mean: 1.052x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 258 ms: 1.01x slower                                                       |
| docutils       | 2.69 sec                                                               | 2.61 sec: 1.03x faster                                                     |
| html5lib       | 65.2 ms                                                                | 62.7 ms: 1.04x faster                                                      |
| sphinx         | 1.05 sec                                                               | 1.00 sec: 1.05x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 979 ms                                                                 | 640 ms: 1.53x faster                                                       |
| async_tree_io              | 851 ms                                                                 | 629 ms: 1.35x faster                                                       |
| async_tree_none_tg         | 324 ms                                                                 | 246 ms: 1.32x faster                                                       |
| async_tree_none            | 330 ms                                                                 | 258 ms: 1.28x faster                                                       |
| async_tree_memoization     | 415 ms                                                                 | 327 ms: 1.27x faster                                                       |
| async_tree_memoization_tg  | 378 ms                                                                 | 319 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                 | 477 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 578 ms                                                                 | 496 ms: 1.16x faster                                                       |
| async_generators           | 430 ms                                                                 | 427 ms: 1.01x faster                                                       |
| coroutines                 | 23.1 ms                                                                | 23.2 ms: 1.01x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.20x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.6 ms                                                                | 79.2 ms: 1.00x faster                                                      |
| pidigits       | 187 ms                                                                 | 188 ms: 1.00x slower                                                       |
| nbody          | 94.7 ms                                                                | 95.1 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.82 ms                                                                | 3.61 ms: 1.06x faster                                                      |
| regex_dna      | 224 ms                                                                 | 218 ms: 1.03x faster                                                       |
| regex_v8       | 25.0 ms                                                                | 24.8 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                                 | 145 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 105 ms                                                                 | 99.7 ms: 1.05x faster                                                      |
| json_dumps           | 11.3 ms                                                                | 11.1 ms: 1.02x faster                                                      |
| json_loads           | 26.4 us                                                                | 26.0 us: 1.02x faster                                                      |
| xml_etree_generate   | 85.5 ms                                                                | 84.6 ms: 1.01x faster                                                      |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                       |
| xml_etree_process    | 59.2 ms                                                                | 58.9 ms: 1.01x faster                                                      |
| tomli_loads          | 2.09 sec                                                               | 2.11 sec: 1.01x slower                                                     |
| pickle_pure_python   | 324 us                                                                 | 328 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.06 ms                                                                | 6.78 ms: 1.04x faster                                                      |
| python_startup         | 12.7 ms                                                                | 12.3 ms: 1.03x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.04x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 22.9 ms                                                                | 22.1 ms: 1.03x faster                                                      |
| genshi_xml     | 50.5 ms                                                                | 50.2 ms: 1.01x faster                                                      |
| mako           | 11.7 ms                                                                | 11.8 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1+-6293d00 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 4.72 ms                                                                | 1.97 ms: 2.40x faster                                                      |
| create_gc_cycles           | 2.70 ms                                                                | 1.70 ms: 1.59x faster                                                      |
| k_core                     | 3.62 sec                                                               | 2.29 sec: 1.58x faster                                                     |
| async_tree_io_tg           | 979 ms                                                                 | 640 ms: 1.53x faster                                                       |
| async_tree_io              | 851 ms                                                                 | 629 ms: 1.35x faster                                                       |
| async_tree_none_tg         | 324 ms                                                                 | 246 ms: 1.32x faster                                                       |
| async_tree_none            | 330 ms                                                                 | 258 ms: 1.28x faster                                                       |
| async_tree_memoization     | 415 ms                                                                 | 327 ms: 1.27x faster                                                       |
| pylint                     | 317 ms                                                                 | 261 ms: 1.21x faster                                                       |
| async_tree_memoization_tg  | 378 ms                                                                 | 319 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                 | 477 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 578 ms                                                                 | 496 ms: 1.16x faster                                                       |
| xml_etree_parse            | 159 ms                                                                 | 145 ms: 1.09x faster                                                       |
| regex_effbot               | 3.82 ms                                                                | 3.61 ms: 1.06x faster                                                      |
| bpe_tokeniser              | 4.82 sec                                                               | 4.56 sec: 1.06x faster                                                     |
| mdp                        | 2.65 sec                                                               | 2.52 sec: 1.05x faster                                                     |
| xml_etree_iterparse        | 105 ms                                                                 | 99.7 ms: 1.05x faster                                                      |
| sphinx                     | 1.05 sec                                                               | 1.00 sec: 1.05x faster                                                     |
| python_startup_no_site     | 7.06 ms                                                                | 6.78 ms: 1.04x faster                                                      |
| html5lib                   | 65.2 ms                                                                | 62.7 ms: 1.04x faster                                                      |
| genshi_text                | 22.9 ms                                                                | 22.1 ms: 1.03x faster                                                      |
| scimark_sor                | 132 ms                                                                 | 127 ms: 1.03x faster                                                       |
| docutils                   | 2.69 sec                                                               | 2.61 sec: 1.03x faster                                                     |
| python_startup             | 12.7 ms                                                                | 12.3 ms: 1.03x faster                                                      |
| regex_dna                  | 224 ms                                                                 | 218 ms: 1.03x faster                                                       |
| sqlalchemy_imperative      | 16.9 ms                                                                | 16.5 ms: 1.02x faster                                                      |
| deepcopy_reduce            | 2.74 us                                                                | 2.68 us: 1.02x faster                                                      |
| generators                 | 28.0 ms                                                                | 27.4 ms: 1.02x faster                                                      |
| json                       | 4.88 ms                                                                | 4.79 ms: 1.02x faster                                                      |
| thrift                     | 782 us                                                                 | 768 us: 1.02x faster                                                       |
| json_dumps                 | 11.3 ms                                                                | 11.1 ms: 1.02x faster                                                      |
| logging_format             | 6.17 us                                                                | 6.06 us: 1.02x faster                                                      |
| json_loads                 | 26.4 us                                                                | 26.0 us: 1.02x faster                                                      |
| pycparser                  | 1.17 sec                                                               | 1.16 sec: 1.01x faster                                                     |
| typing_runtime_protocols   | 161 us                                                                 | 159 us: 1.01x faster                                                       |
| logging_simple             | 5.60 us                                                                | 5.52 us: 1.01x faster                                                      |
| fannkuch                   | 410 ms                                                                 | 405 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.5 ms                                                                | 84.6 ms: 1.01x faster                                                      |
| comprehensions             | 17.0 us                                                                | 16.8 us: 1.01x faster                                                      |
| telco                      | 7.84 ms                                                                | 7.77 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                                       |
| async_generators           | 430 ms                                                                 | 427 ms: 1.01x faster                                                       |
| regex_v8                   | 25.0 ms                                                                | 24.8 ms: 1.01x faster                                                      |
| pyflate                    | 470 ms                                                                 | 466 ms: 1.01x faster                                                       |
| scimark_lu                 | 117 ms                                                                 | 116 ms: 1.01x faster                                                       |
| deltablue                  | 3.34 ms                                                                | 3.32 ms: 1.01x faster                                                      |
| xml_etree_process          | 59.2 ms                                                                | 58.9 ms: 1.01x faster                                                      |
| genshi_xml                 | 50.5 ms                                                                | 50.2 ms: 1.01x faster                                                      |
| float                      | 79.6 ms                                                                | 79.2 ms: 1.00x faster                                                      |
| sqlalchemy_declarative     | 128 ms                                                                 | 127 ms: 1.00x faster                                                       |
| deepcopy                   | 263 us                                                                 | 262 us: 1.00x faster                                                       |
| go                         | 121 ms                                                                 | 121 ms: 1.00x faster                                                       |
| pidigits                   | 187 ms                                                                 | 188 ms: 1.00x slower                                                       |
| bench_thread_pool          | 850 us                                                                 | 852 us: 1.00x slower                                                       |
| nbody                      | 94.7 ms                                                                | 95.1 ms: 1.00x slower                                                      |
| chaos                      | 61.1 ms                                                                | 61.5 ms: 1.01x slower                                                      |
| nqueens                    | 80.7 ms                                                                | 81.2 ms: 1.01x slower                                                      |
| coroutines                 | 23.1 ms                                                                | 23.2 ms: 1.01x slower                                                      |
| hexiom                     | 6.32 ms                                                                | 6.37 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 53.7 ms                                                                | 54.1 ms: 1.01x slower                                                      |
| richards                   | 45.6 ms                                                                | 45.9 ms: 1.01x slower                                                      |
| 2to3                       | 256 ms                                                                 | 258 ms: 1.01x slower                                                       |
| deepcopy_memo              | 30.4 us                                                                | 30.7 us: 1.01x slower                                                      |
| tomli_loads                | 2.09 sec                                                               | 2.11 sec: 1.01x slower                                                     |
| pathlib                    | 16.1 ms                                                                | 16.3 ms: 1.01x slower                                                      |
| mako                       | 11.7 ms                                                                | 11.8 ms: 1.01x slower                                                      |
| dulwich_log                | 64.5 ms                                                                | 65.2 ms: 1.01x slower                                                      |
| sqlglot_parse              | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                                      |
| logging_silent             | 105 ns                                                                 | 106 ns: 1.01x slower                                                       |
| pickle_pure_python         | 324 us                                                                 | 328 us: 1.01x slower                                                       |
| sqlglot_normalize          | 107 ms                                                                 | 108 ms: 1.01x slower                                                       |
| richards_super             | 51.8 ms                                                                | 52.6 ms: 1.02x slower                                                      |
| sqlglot_transpile          | 1.59 ms                                                                | 1.62 ms: 1.02x slower                                                      |
| crypto_pyaes               | 71.7 ms                                                                | 73.0 ms: 1.02x slower                                                      |
| bench_mp_pool              | 79.0 ms                                                                | 80.7 ms: 1.02x slower                                                      |
| scimark_fft                | 369 ms                                                                 | 380 ms: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 4.96 ms                                                                | 5.17 ms: 1.04x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (17): spectral_norm, sympy_expand, sympy_sum, shortest_path, sympy_integrate, meteor_contest, asyncio_websockets, regex_compile, scimark_monte_carlo, pprint_safe_repr, sqlite_synth, raytrace, sympy_str, pprint_pformat, connected_components, django_template, coverage

- Geometric mean (including insignificant results): 1.052x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x