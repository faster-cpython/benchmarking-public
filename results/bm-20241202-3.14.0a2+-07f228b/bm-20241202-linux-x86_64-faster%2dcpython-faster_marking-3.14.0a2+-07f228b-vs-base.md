# Results vs. base

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 07f228b
- commit date: 2024-12-02
- overall geometric mean: 1.010x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 256 ms: 1.01x slower                                                       |
| html5lib       | 63.1 ms                                                                | 63.8 ms: 1.01x slower                                                      |
| sphinx         | 1.02 sec                                                               | 1.03 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators           | 429 ms                                                                 | 424 ms: 1.01x faster                                                       |
| coroutines                 | 23.5 ms                                                                | 23.8 ms: 1.02x slower                                                      |
| async_tree_memoization     | 341 ms                                                                 | 352 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed    | 502 ms                                                                 | 522 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 514 ms: 1.05x slower                                                       |
| async_tree_none            | 271 ms                                                                 | 289 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 626 ms                                                                 | 683 ms: 1.09x slower                                                       |
| async_tree_memoization_tg  | 315 ms                                                                 | 352 ms: 1.12x slower                                                       |
| async_tree_none_tg         | 252 ms                                                                 | 286 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.05x slower                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                       |
| nbody          | 94.0 ms                                                                | 94.5 ms: 1.01x slower                                                      |
| float          | 78.0 ms                                                                | 79.6 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.45 ms                                                                | 3.35 ms: 1.03x faster                                                      |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                       |
| regex_v8       | 25.2 ms                                                                | 25.9 ms: 1.03x slower                                                      |
| regex_dna      | 213 ms                                                                 | 222 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 27.0 us                                                                | 26.1 us: 1.03x faster                                                      |
| tomli_loads          | 2.11 sec                                                               | 2.08 sec: 1.01x faster                                                     |
| json_dumps           | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                                      |
| pickle_pure_python   | 328 us                                                                 | 330 us: 1.01x slower                                                       |
| unpickle_pure_python | 219 us                                                                 | 220 us: 1.01x slower                                                       |
| xml_etree_process    | 59.0 ms                                                                | 60.2 ms: 1.02x slower                                                      |
| xml_etree_generate   | 83.8 ms                                                                | 86.5 ms: 1.03x slower                                                      |
| xml_etree_parse      | 139 ms                                                                 | 148 ms: 1.06x slower                                                       |
| xml_etree_iterparse  | 96.9 ms                                                                | 104 ms: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                                | 12.8 ms: 1.00x slower                                                      |
| python_startup_no_site | 7.02 ms                                                                | 7.06 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 32.2 ms                                                                | 31.8 ms: 1.01x faster                                                      |
| genshi_text     | 22.4 ms                                                                | 22.7 ms: 1.01x slower                                                      |
| mako            | 11.2 ms                                                                | 11.6 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads                 | 27.0 us                                                                | 26.1 us: 1.03x faster                                                      |
| pyflate                    | 468 ms                                                                 | 453 ms: 1.03x faster                                                       |
| regex_effbot               | 3.45 ms                                                                | 3.35 ms: 1.03x faster                                                      |
| json                       | 5.00 ms                                                                | 4.85 ms: 1.03x faster                                                      |
| gc_traversal               | 4.79 ms                                                                | 4.66 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 4.84 ms                                                                | 4.75 ms: 1.02x faster                                                      |
| create_gc_cycles           | 2.47 ms                                                                | 2.43 ms: 1.02x faster                                                      |
| pprint_pformat             | 1.52 sec                                                               | 1.50 sec: 1.01x faster                                                     |
| tomli_loads                | 2.11 sec                                                               | 2.08 sec: 1.01x faster                                                     |
| go                         | 119 ms                                                                 | 118 ms: 1.01x faster                                                       |
| sqlite_synth               | 2.90 us                                                                | 2.86 us: 1.01x faster                                                      |
| django_template            | 32.2 ms                                                                | 31.8 ms: 1.01x faster                                                      |
| async_generators           | 429 ms                                                                 | 424 ms: 1.01x faster                                                       |
| deltablue                  | 3.27 ms                                                                | 3.23 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 744 ms                                                                 | 736 ms: 1.01x faster                                                       |
| deepcopy_reduce            | 2.72 us                                                                | 2.69 us: 1.01x faster                                                      |
| comprehensions             | 17.0 us                                                                | 16.9 us: 1.01x faster                                                      |
| richards                   | 47.3 ms                                                                | 46.8 ms: 1.01x faster                                                      |
| raytrace                   | 272 ms                                                                 | 270 ms: 1.01x faster                                                       |
| dulwich_log                | 64.6 ms                                                                | 64.0 ms: 1.01x faster                                                      |
| json_dumps                 | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                                      |
| generators                 | 28.0 ms                                                                | 27.8 ms: 1.01x faster                                                      |
| meteor_contest             | 107 ms                                                                 | 107 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 107 ms                                                                 | 106 ms: 1.01x faster                                                       |
| richards_super             | 53.4 ms                                                                | 53.1 ms: 1.00x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                                | 68.8 ms: 1.00x faster                                                      |
| pidigits                   | 186 ms                                                                 | 187 ms: 1.00x slower                                                       |
| sympy_integrate            | 19.8 ms                                                                | 19.9 ms: 1.00x slower                                                      |
| coverage                   | 83.1 ms                                                                | 83.4 ms: 1.00x slower                                                      |
| python_startup             | 12.7 ms                                                                | 12.8 ms: 1.00x slower                                                      |
| sympy_sum                  | 148 ms                                                                 | 148 ms: 1.00x slower                                                       |
| python_startup_no_site     | 7.02 ms                                                                | 7.06 ms: 1.01x slower                                                      |
| subparsers                 | 20.7 ms                                                                | 20.8 ms: 1.01x slower                                                      |
| nbody                      | 94.0 ms                                                                | 94.5 ms: 1.01x slower                                                      |
| pickle_pure_python         | 328 us                                                                 | 330 us: 1.01x slower                                                       |
| deepcopy_memo              | 30.6 us                                                                | 30.8 us: 1.01x slower                                                      |
| logging_simple             | 5.56 us                                                                | 5.60 us: 1.01x slower                                                      |
| unpickle_pure_python       | 219 us                                                                 | 220 us: 1.01x slower                                                       |
| 2to3                       | 254 ms                                                                 | 256 ms: 1.01x slower                                                       |
| regex_compile              | 128 ms                                                                 | 129 ms: 1.01x slower                                                       |
| fannkuch                   | 406 ms                                                                 | 409 ms: 1.01x slower                                                       |
| scimark_fft                | 364 ms                                                                 | 367 ms: 1.01x slower                                                       |
| sympy_str                  | 269 ms                                                                 | 271 ms: 1.01x slower                                                       |
| crypto_pyaes               | 72.3 ms                                                                | 72.9 ms: 1.01x slower                                                      |
| html5lib                   | 63.1 ms                                                                | 63.8 ms: 1.01x slower                                                      |
| logging_silent             | 107 ns                                                                 | 108 ns: 1.01x slower                                                       |
| sphinx                     | 1.02 sec                                                               | 1.03 sec: 1.01x slower                                                     |
| nqueens                    | 80.2 ms                                                                | 81.3 ms: 1.01x slower                                                      |
| many_optionals             | 939 us                                                                 | 952 us: 1.01x slower                                                       |
| genshi_text                | 22.4 ms                                                                | 22.7 ms: 1.01x slower                                                      |
| hexiom                     | 6.23 ms                                                                | 6.32 ms: 1.01x slower                                                      |
| sqlglot_parse              | 1.29 ms                                                                | 1.30 ms: 1.02x slower                                                      |
| coroutines                 | 23.5 ms                                                                | 23.8 ms: 1.02x slower                                                      |
| scimark_sor                | 127 ms                                                                 | 129 ms: 1.02x slower                                                       |
| float                      | 78.0 ms                                                                | 79.6 ms: 1.02x slower                                                      |
| xml_etree_process          | 59.0 ms                                                                | 60.2 ms: 1.02x slower                                                      |
| scimark_lu                 | 115 ms                                                                 | 118 ms: 1.02x slower                                                       |
| pycparser                  | 1.13 sec                                                               | 1.16 sec: 1.02x slower                                                     |
| bpe_tokeniser              | 4.51 sec                                                               | 4.63 sec: 1.03x slower                                                     |
| regex_v8                   | 25.2 ms                                                                | 25.9 ms: 1.03x slower                                                      |
| xml_etree_generate         | 83.8 ms                                                                | 86.5 ms: 1.03x slower                                                      |
| async_tree_memoization     | 341 ms                                                                 | 352 ms: 1.03x slower                                                       |
| mako                       | 11.2 ms                                                                | 11.6 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed    | 502 ms                                                                 | 522 ms: 1.04x slower                                                       |
| djangocms                  | 21.6 us                                                                | 22.5 us: 1.04x slower                                                      |
| regex_dna                  | 213 ms                                                                 | 222 ms: 1.04x slower                                                       |
| k_core                     | 2.29 sec                                                               | 2.40 sec: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 514 ms: 1.05x slower                                                       |
| mdp                        | 2.55 sec                                                               | 2.69 sec: 1.06x slower                                                     |
| xml_etree_parse            | 139 ms                                                                 | 148 ms: 1.06x slower                                                       |
| async_tree_none            | 271 ms                                                                 | 289 ms: 1.07x slower                                                       |
| spectral_norm              | 111 ms                                                                 | 119 ms: 1.07x slower                                                       |
| xml_etree_iterparse        | 96.9 ms                                                                | 104 ms: 1.08x slower                                                       |
| async_tree_io_tg           | 626 ms                                                                 | 683 ms: 1.09x slower                                                       |
| async_tree_memoization_tg  | 315 ms                                                                 | 352 ms: 1.12x slower                                                       |
| async_tree_none_tg         | 252 ms                                                                 | 286 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (21): pylint, telco, sqlglot_optimize, typing_runtime_protocols, connected_components, bench_mp_pool, thrift, docutils, pathlib, logging_format, genshi_xml, shortest_path, sqlalchemy_declarative, sqlglot_transpile, bench_thread_pool, chaos, deepcopy, asyncio_websockets, sympy_expand, async_tree_io, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x