# Results vs. base

- fork: faster-cpython
- ref: mark_first_gc
- machine: linux-x86_64
- commit hash: 5e813c5
- commit date: 2024-11-04
- overall geometric mean: 1.021x faster
- HPT reliability: 54.09%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 256 ms: 1.00x slower                                                      |
| docutils       | 2.70 sec                                                               | 2.62 sec: 1.03x faster                                                    |
| html5lib       | 64.0 ms                                                                | 63.6 ms: 1.01x faster                                                     |
| sphinx         | 1.05 sec                                                               | 1.01 sec: 1.04x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 962 ms                                                                 | 658 ms: 1.46x faster                                                      |
| async_tree_io              | 855 ms                                                                 | 637 ms: 1.34x faster                                                      |
| async_tree_none_tg         | 321 ms                                                                 | 254 ms: 1.26x faster                                                      |
| async_tree_none            | 326 ms                                                                 | 268 ms: 1.22x faster                                                      |
| async_tree_memoization     | 413 ms                                                                 | 339 ms: 1.22x faster                                                      |
| async_tree_memoization_tg  | 375 ms                                                                 | 316 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                 | 479 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                                 | 495 ms: 1.17x faster                                                      |
| coroutines                 | 23.4 ms                                                                | 24.3 ms: 1.04x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.17x faster                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 80.3 ms                                                                | 77.7 ms: 1.03x faster                                                     |
| pidigits       | 187 ms                                                                 | 188 ms: 1.00x slower                                                      |
| nbody          | 95.0 ms                                                                | 101 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.65 ms                                                                | 3.54 ms: 1.03x faster                                                     |
| regex_dna      | 215 ms                                                                 | 210 ms: 1.02x faster                                                      |
| regex_v8       | 25.3 ms                                                                | 25.1 ms: 1.00x faster                                                     |
| regex_compile  | 129 ms                                                                 | 129 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 158 ms                                                                 | 151 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 105 ms                                                                 | 101 ms: 1.04x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                                | 85.2 ms: 1.01x faster                                                     |
| json_dumps           | 11.2 ms                                                                | 11.3 ms: 1.01x slower                                                     |
| unpickle_pure_python | 218 us                                                                 | 223 us: 1.02x slower                                                      |
| tomli_loads          | 2.06 sec                                                               | 2.11 sec: 1.03x slower                                                    |
| json_loads           | 26.2 us                                                                | 27.0 us: 1.03x slower                                                     |
| pickle_pure_python   | 320 us                                                                 | 330 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.07 ms                                                                | 7.04 ms: 1.00x faster                                                     |
| python_startup         | 12.7 ms                                                                | 12.7 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                                | 22.5 ms: 1.01x faster                                                     |
| mako            | 11.5 ms                                                                | 11.5 ms: 1.00x faster                                                     |
| django_template | 34.0 ms                                                                | 34.6 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 962 ms                                                                 | 658 ms: 1.46x faster                                                      |
| k_core                     | 3.63 sec                                                               | 2.63 sec: 1.38x faster                                                    |
| async_tree_io              | 855 ms                                                                 | 637 ms: 1.34x faster                                                      |
| async_tree_none_tg         | 321 ms                                                                 | 254 ms: 1.26x faster                                                      |
| async_tree_none            | 326 ms                                                                 | 268 ms: 1.22x faster                                                      |
| async_tree_memoization     | 413 ms                                                                 | 339 ms: 1.22x faster                                                      |
| async_tree_memoization_tg  | 375 ms                                                                 | 316 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                 | 479 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                                 | 495 ms: 1.17x faster                                                      |
| pylint                     | 319 ms                                                                 | 279 ms: 1.14x faster                                                      |
| gc_traversal               | 4.80 ms                                                                | 4.47 ms: 1.07x faster                                                     |
| xml_etree_parse            | 158 ms                                                                 | 151 ms: 1.05x faster                                                      |
| bpe_tokeniser              | 4.78 sec                                                               | 4.57 sec: 1.05x faster                                                    |
| create_gc_cycles           | 2.70 ms                                                                | 2.58 ms: 1.05x faster                                                     |
| sphinx                     | 1.05 sec                                                               | 1.01 sec: 1.04x faster                                                    |
| xml_etree_iterparse        | 105 ms                                                                 | 101 ms: 1.04x faster                                                      |
| pyflate                    | 476 ms                                                                 | 461 ms: 1.03x faster                                                      |
| float                      | 80.3 ms                                                                | 77.7 ms: 1.03x faster                                                     |
| regex_effbot               | 3.65 ms                                                                | 3.54 ms: 1.03x faster                                                     |
| docutils                   | 2.70 sec                                                               | 2.62 sec: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 5.12 ms                                                                | 4.98 ms: 1.03x faster                                                     |
| regex_dna                  | 215 ms                                                                 | 210 ms: 1.02x faster                                                      |
| telco                      | 8.07 ms                                                                | 7.94 ms: 1.02x faster                                                     |
| pycparser                  | 1.19 sec                                                               | 1.17 sec: 1.01x faster                                                    |
| genshi_text                | 22.6 ms                                                                | 22.5 ms: 1.01x faster                                                     |
| html5lib                   | 64.0 ms                                                                | 63.6 ms: 1.01x faster                                                     |
| xml_etree_generate         | 85.7 ms                                                                | 85.2 ms: 1.01x faster                                                     |
| regex_v8                   | 25.3 ms                                                                | 25.1 ms: 1.00x faster                                                     |
| python_startup_no_site     | 7.07 ms                                                                | 7.04 ms: 1.00x faster                                                     |
| dulwich_log                | 64.4 ms                                                                | 64.2 ms: 1.00x faster                                                     |
| mako                       | 11.5 ms                                                                | 11.5 ms: 1.00x faster                                                     |
| python_startup             | 12.7 ms                                                                | 12.7 ms: 1.00x faster                                                     |
| pidigits                   | 187 ms                                                                 | 188 ms: 1.00x slower                                                      |
| regex_compile              | 129 ms                                                                 | 129 ms: 1.00x slower                                                      |
| sympy_integrate            | 19.8 ms                                                                | 19.9 ms: 1.00x slower                                                     |
| go                         | 121 ms                                                                 | 121 ms: 1.00x slower                                                      |
| 2to3                       | 255 ms                                                                 | 256 ms: 1.00x slower                                                      |
| sqlglot_optimize           | 53.4 ms                                                                | 53.6 ms: 1.00x slower                                                     |
| bench_thread_pool          | 837 us                                                                 | 840 us: 1.00x slower                                                      |
| comprehensions             | 16.9 us                                                                | 17.0 us: 1.00x slower                                                     |
| sympy_str                  | 267 ms                                                                 | 268 ms: 1.01x slower                                                      |
| sqlglot_parse              | 1.30 ms                                                                | 1.31 ms: 1.01x slower                                                     |
| pprint_pformat             | 1.48 sec                                                               | 1.49 sec: 1.01x slower                                                    |
| json_dumps                 | 11.2 ms                                                                | 11.3 ms: 1.01x slower                                                     |
| sympy_sum                  | 146 ms                                                                 | 148 ms: 1.01x slower                                                      |
| sqlalchemy_declarative     | 127 ms                                                                 | 128 ms: 1.01x slower                                                      |
| fannkuch                   | 403 ms                                                                 | 407 ms: 1.01x slower                                                      |
| chaos                      | 61.0 ms                                                                | 61.7 ms: 1.01x slower                                                     |
| scimark_monte_carlo        | 69.1 ms                                                                | 69.9 ms: 1.01x slower                                                     |
| sqlglot_transpile          | 1.60 ms                                                                | 1.62 ms: 1.01x slower                                                     |
| thrift                     | 767 us                                                                 | 777 us: 1.01x slower                                                      |
| logging_format             | 6.06 us                                                                | 6.14 us: 1.01x slower                                                     |
| scimark_sor                | 126 ms                                                                 | 128 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 725 ms                                                                 | 736 ms: 1.01x slower                                                      |
| django_template            | 34.0 ms                                                                | 34.6 ms: 1.02x slower                                                     |
| hexiom                     | 6.27 ms                                                                | 6.36 ms: 1.02x slower                                                     |
| raytrace                   | 274 ms                                                                 | 278 ms: 1.02x slower                                                      |
| scimark_lu                 | 116 ms                                                                 | 119 ms: 1.02x slower                                                      |
| sqlite_synth               | 2.82 us                                                                | 2.89 us: 1.02x slower                                                     |
| unpickle_pure_python       | 218 us                                                                 | 223 us: 1.02x slower                                                      |
| nqueens                    | 79.0 ms                                                                | 81.0 ms: 1.03x slower                                                     |
| tomli_loads                | 2.06 sec                                                               | 2.11 sec: 1.03x slower                                                    |
| spectral_norm              | 115 ms                                                                 | 118 ms: 1.03x slower                                                      |
| json_loads                 | 26.2 us                                                                | 27.0 us: 1.03x slower                                                     |
| deepcopy                   | 262 us                                                                 | 270 us: 1.03x slower                                                      |
| crypto_pyaes               | 72.1 ms                                                                | 74.4 ms: 1.03x slower                                                     |
| pickle_pure_python         | 320 us                                                                 | 330 us: 1.03x slower                                                      |
| generators                 | 27.1 ms                                                                | 28.1 ms: 1.04x slower                                                     |
| deepcopy_reduce            | 2.70 us                                                                | 2.80 us: 1.04x slower                                                     |
| coroutines                 | 23.4 ms                                                                | 24.3 ms: 1.04x slower                                                     |
| json                       | 4.82 ms                                                                | 5.02 ms: 1.04x slower                                                     |
| richards                   | 46.3 ms                                                                | 48.2 ms: 1.04x slower                                                     |
| logging_silent             | 105 ns                                                                 | 110 ns: 1.04x slower                                                      |
| richards_super             | 52.3 ms                                                                | 54.6 ms: 1.04x slower                                                     |
| deepcopy_memo              | 30.6 us                                                                | 32.0 us: 1.05x slower                                                     |
| scimark_fft                | 368 ms                                                                 | 387 ms: 1.05x slower                                                      |
| nbody                      | 95.0 ms                                                                | 101 ms: 1.07x slower                                                      |
| mdp                        | 2.49 sec                                                               | 2.71 sec: 1.09x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (16): sqlalchemy_imperative, sympy_expand, connected_components, shortest_path, meteor_contest, typing_runtime_protocols, coverage, asyncio_websockets, deltablue, bench_mp_pool, xml_etree_process, sqlglot_normalize, genshi_xml, async_generators, logging_simple, pathlib

- Geometric mean (including insignificant results): 1.021x faster
# HPT report

- Reliability score: 54.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x