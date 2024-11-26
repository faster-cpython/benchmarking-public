# Results vs. base

- fork: brandtbucher
- ref: jb0_invalidate
- machine: linux-x86_64
- commit hash: 69e9a0e
- commit date: 2024-10-24
- overall geometric mean: 1.050x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                 | 284 ms: 1.02x slower                                                   |
| docutils       | 2.91 sec                                                               | 3.36 sec: 1.15x slower                                                 |
| html5lib       | 65.2 ms                                                                | 69.9 ms: 1.07x slower                                                  |
| sphinx         | 1.17 sec                                                               | 1.32 sec: 1.13x slower                                                 |
| tornado_http   | 94.6 ms                                                                | 112 ms: 1.19x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.11x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 977 ms                                                                 | 953 ms: 1.02x faster                                                   |
| async_generators           | 460 ms                                                                 | 462 ms: 1.00x slower                                                   |
| asyncio_websockets         | 554 ms                                                                 | 559 ms: 1.01x slower                                                   |
| async_tree_none            | 336 ms                                                                 | 347 ms: 1.03x slower                                                   |
| async_tree_none_tg         | 322 ms                                                                 | 332 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed    | 577 ms                                                                 | 599 ms: 1.04x slower                                                   |
| async_tree_memoization     | 416 ms                                                                 | 434 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 589 ms: 1.05x slower                                                   |
| async_tree_memoization_tg  | 380 ms                                                                 | 407 ms: 1.07x slower                                                   |
| async_tree_io              | 855 ms                                                                 | 950 ms: 1.11x slower                                                   |
| coroutines                 | 23.1 ms                                                                | 26.5 ms: 1.15x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.05x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.1 ms                                                                | 75.3 ms: 1.01x faster                                                  |
| pidigits       | 187 ms                                                                 | 188 ms: 1.01x slower                                                   |
| nbody          | 81.7 ms                                                                | 82.4 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                | 3.74 ms: 1.01x faster                                                  |
| regex_dna      | 217 ms                                                                 | 220 ms: 1.02x slower                                                   |
| regex_v8       | 24.7 ms                                                                | 25.5 ms: 1.03x slower                                                  |
| regex_compile  | 139 ms                                                                 | 147 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 316 us                                                                 | 295 us: 1.07x faster                                                   |
| xml_etree_iterparse  | 100 ms                                                                 | 99.4 ms: 1.01x faster                                                  |
| json_dumps           | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                                  |
| json_loads           | 26.6 us                                                                | 27.0 us: 1.01x slower                                                  |
| tomli_loads          | 1.92 sec                                                               | 1.99 sec: 1.03x slower                                                 |
| unpickle_pure_python | 216 us                                                                 | 225 us: 1.04x slower                                                   |
| xml_etree_generate   | 78.4 ms                                                                | 83.2 ms: 1.06x slower                                                  |
| xml_etree_process    | 55.3 ms                                                                | 59.8 ms: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.8 ms                                                                | 11.9 ms: 1.01x slower                                                  |
| python_startup_no_site | 7.05 ms                                                                | 7.22 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 61.8 ms                                                                | 62.9 ms: 1.02x slower                                                  |
| mako            | 9.87 ms                                                                | 10.6 ms: 1.07x slower                                                  |
| django_template | 37.1 ms                                                                | 40.1 ms: 1.08x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.04x slower                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python         | 316 us                                                                 | 295 us: 1.07x faster                                                   |
| scimark_monte_carlo        | 64.5 ms                                                                | 62.4 ms: 1.03x faster                                                  |
| go                         | 133 ms                                                                 | 129 ms: 1.03x faster                                                   |
| async_tree_io_tg           | 977 ms                                                                 | 953 ms: 1.02x faster                                                   |
| scimark_lu                 | 115 ms                                                                 | 113 ms: 1.02x faster                                                   |
| typing_runtime_protocols   | 169 us                                                                 | 165 us: 1.02x faster                                                   |
| scimark_fft                | 323 ms                                                                 | 319 ms: 1.01x faster                                                   |
| float                      | 76.1 ms                                                                | 75.3 ms: 1.01x faster                                                  |
| xml_etree_iterparse        | 100 ms                                                                 | 99.4 ms: 1.01x faster                                                  |
| regex_effbot               | 3.77 ms                                                                | 3.74 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                                 | 108 ms: 1.01x faster                                                   |
| async_generators           | 460 ms                                                                 | 462 ms: 1.00x slower                                                   |
| pidigits                   | 187 ms                                                                 | 188 ms: 1.01x slower                                                   |
| fannkuch                   | 376 ms                                                                 | 378 ms: 1.01x slower                                                   |
| create_gc_cycles           | 2.67 ms                                                                | 2.69 ms: 1.01x slower                                                  |
| nbody                      | 81.7 ms                                                                | 82.4 ms: 1.01x slower                                                  |
| asyncio_websockets         | 554 ms                                                                 | 559 ms: 1.01x slower                                                   |
| json_dumps                 | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                                  |
| crypto_pyaes               | 68.3 ms                                                                | 69.1 ms: 1.01x slower                                                  |
| json_loads                 | 26.6 us                                                                | 27.0 us: 1.01x slower                                                  |
| python_startup             | 11.8 ms                                                                | 11.9 ms: 1.01x slower                                                  |
| bpe_tokeniser              | 4.44 sec                                                               | 4.50 sec: 1.01x slower                                                 |
| regex_dna                  | 217 ms                                                                 | 220 ms: 1.02x slower                                                   |
| genshi_xml                 | 61.8 ms                                                                | 62.9 ms: 1.02x slower                                                  |
| pprint_pformat             | 1.48 sec                                                               | 1.50 sec: 1.02x slower                                                 |
| json                       | 4.98 ms                                                                | 5.08 ms: 1.02x slower                                                  |
| 2to3                       | 279 ms                                                                 | 284 ms: 1.02x slower                                                   |
| scimark_sor                | 119 ms                                                                 | 121 ms: 1.02x slower                                                   |
| deepcopy                   | 269 us                                                                 | 275 us: 1.02x slower                                                   |
| python_startup_no_site     | 7.05 ms                                                                | 7.22 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult    | 4.60 ms                                                                | 4.73 ms: 1.03x slower                                                  |
| coverage                   | 84.4 ms                                                                | 86.9 ms: 1.03x slower                                                  |
| deepcopy_memo              | 29.3 us                                                                | 30.2 us: 1.03x slower                                                  |
| async_tree_none            | 336 ms                                                                 | 347 ms: 1.03x slower                                                   |
| async_tree_none_tg         | 322 ms                                                                 | 332 ms: 1.03x slower                                                   |
| generators                 | 35.5 ms                                                                | 36.7 ms: 1.03x slower                                                  |
| pathlib                    | 16.2 ms                                                                | 16.8 ms: 1.03x slower                                                  |
| sqlglot_normalize          | 115 ms                                                                 | 119 ms: 1.03x slower                                                   |
| tomli_loads                | 1.92 sec                                                               | 1.99 sec: 1.03x slower                                                 |
| regex_v8                   | 24.7 ms                                                                | 25.5 ms: 1.03x slower                                                  |
| dulwich_log                | 66.4 ms                                                                | 68.7 ms: 1.04x slower                                                  |
| deepcopy_reduce            | 2.77 us                                                                | 2.87 us: 1.04x slower                                                  |
| unpickle_pure_python       | 216 us                                                                 | 225 us: 1.04x slower                                                   |
| async_tree_cpu_io_mixed    | 577 ms                                                                 | 599 ms: 1.04x slower                                                   |
| async_tree_memoization     | 416 ms                                                                 | 434 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 589 ms: 1.05x slower                                                   |
| pyflate                    | 445 ms                                                                 | 466 ms: 1.05x slower                                                   |
| comprehensions             | 17.0 us                                                                | 17.9 us: 1.05x slower                                                  |
| thrift                     | 789 us                                                                 | 829 us: 1.05x slower                                                   |
| raytrace                   | 283 ms                                                                 | 299 ms: 1.06x slower                                                   |
| xml_etree_generate         | 78.4 ms                                                                | 83.2 ms: 1.06x slower                                                  |
| regex_compile              | 139 ms                                                                 | 147 ms: 1.06x slower                                                   |
| sympy_expand               | 503 ms                                                                 | 536 ms: 1.07x slower                                                   |
| bench_mp_pool              | 83.7 ms                                                                | 89.3 ms: 1.07x slower                                                  |
| sqlglot_parse              | 1.34 ms                                                                | 1.43 ms: 1.07x slower                                                  |
| html5lib                   | 65.2 ms                                                                | 69.9 ms: 1.07x slower                                                  |
| mako                       | 9.87 ms                                                                | 10.6 ms: 1.07x slower                                                  |
| async_tree_memoization_tg  | 380 ms                                                                 | 407 ms: 1.07x slower                                                   |
| django_template            | 37.1 ms                                                                | 40.1 ms: 1.08x slower                                                  |
| xml_etree_process          | 55.3 ms                                                                | 59.8 ms: 1.08x slower                                                  |
| sqlglot_optimize           | 60.1 ms                                                                | 65.1 ms: 1.08x slower                                                  |
| sqlglot_transpile          | 1.71 ms                                                                | 1.85 ms: 1.08x slower                                                  |
| mdp                        | 2.57 sec                                                               | 2.81 sec: 1.09x slower                                                 |
| sympy_str                  | 306 ms                                                                 | 335 ms: 1.09x slower                                                   |
| bench_thread_pool          | 877 us                                                                 | 967 us: 1.10x slower                                                   |
| async_tree_io              | 855 ms                                                                 | 950 ms: 1.11x slower                                                   |
| sympy_integrate            | 23.6 ms                                                                | 26.5 ms: 1.12x slower                                                  |
| pycparser                  | 1.15 sec                                                               | 1.31 sec: 1.13x slower                                                 |
| sphinx                     | 1.17 sec                                                               | 1.32 sec: 1.13x slower                                                 |
| coroutines                 | 23.1 ms                                                                | 26.5 ms: 1.15x slower                                                  |
| docutils                   | 2.91 sec                                                               | 3.36 sec: 1.15x slower                                                 |
| sqlalchemy_declarative     | 147 ms                                                                 | 174 ms: 1.18x slower                                                   |
| sympy_sum                  | 177 ms                                                                 | 209 ms: 1.18x slower                                                   |
| tornado_http               | 94.6 ms                                                                | 112 ms: 1.19x slower                                                   |
| richards                   | 41.8 ms                                                                | 49.6 ms: 1.19x slower                                                  |
| richards_super             | 45.5 ms                                                                | 55.4 ms: 1.22x slower                                                  |
| logging_format             | 6.22 us                                                                | 7.61 us: 1.22x slower                                                  |
| logging_simple             | 5.61 us                                                                | 7.01 us: 1.25x slower                                                  |
| deltablue                  | 3.23 ms                                                                | 4.04 ms: 1.25x slower                                                  |
| sqlalchemy_imperative      | 17.8 ms                                                                | 22.7 ms: 1.27x slower                                                  |
| pylint                     | 325 ms                                                                 | 460 ms: 1.41x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (10): chaos, xml_etree_parse, genshi_text, spectral_norm, gc_traversal, pprint_safe_repr, telco, logging_silent, nqueens, hexiom

- Geometric mean (including insignificant results): 1.050x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.05x