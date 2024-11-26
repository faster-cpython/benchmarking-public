# Results vs. base

- fork: brandtbucher
- ref: jb0_backoff
- machine: linux-x86_64
- commit hash: 50d9e07
- commit date: 2024-10-24
- overall geometric mean: 1.047x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                 | 286 ms: 1.03x slower                                                |
| docutils       | 2.91 sec                                                               | 3.40 sec: 1.17x slower                                              |
| html5lib       | 65.2 ms                                                                | 68.6 ms: 1.05x slower                                               |
| sphinx         | 1.17 sec                                                               | 1.35 sec: 1.15x slower                                              |
| tornado_http   | 94.6 ms                                                                | 112 ms: 1.18x slower                                                |
| Geometric mean | (ref)                                                                  | 1.11x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 977 ms                                                                 | 959 ms: 1.02x faster                                                |
| asyncio_websockets         | 554 ms                                                                 | 557 ms: 1.01x slower                                                |
| async_generators           | 460 ms                                                                 | 467 ms: 1.02x slower                                                |
| async_tree_none            | 336 ms                                                                 | 347 ms: 1.03x slower                                                |
| async_tree_cpu_io_mixed    | 577 ms                                                                 | 599 ms: 1.04x slower                                                |
| async_tree_memoization     | 416 ms                                                                 | 434 ms: 1.05x slower                                                |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 589 ms: 1.05x slower                                                |
| async_tree_none_tg         | 322 ms                                                                 | 338 ms: 1.05x slower                                                |
| async_tree_memoization_tg  | 380 ms                                                                 | 405 ms: 1.07x slower                                                |
| async_tree_io              | 855 ms                                                                 | 941 ms: 1.10x slower                                                |
| coroutines                 | 23.1 ms                                                                | 26.4 ms: 1.14x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.05x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.1 ms                                                                | 75.0 ms: 1.01x faster                                               |
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                | 3.71 ms: 1.02x faster                                               |
| regex_dna      | 217 ms                                                                 | 215 ms: 1.01x faster                                                |
| regex_v8       | 24.7 ms                                                                | 25.8 ms: 1.05x slower                                               |
| regex_compile  | 139 ms                                                                 | 146 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 316 us                                                                 | 294 us: 1.08x faster                                                |
| xml_etree_parse      | 149 ms                                                                 | 146 ms: 1.02x faster                                                |
| json_loads           | 26.6 us                                                                | 26.7 us: 1.00x slower                                               |
| json_dumps           | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                               |
| tomli_loads          | 1.92 sec                                                               | 1.94 sec: 1.01x slower                                              |
| unpickle_pure_python | 216 us                                                                 | 226 us: 1.04x slower                                                |
| xml_etree_generate   | 78.4 ms                                                                | 83.3 ms: 1.06x slower                                               |
| xml_etree_process    | 55.3 ms                                                                | 60.1 ms: 1.09x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.11 ms: 1.01x slower                                               |
| python_startup         | 11.8 ms                                                                | 11.9 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 26.3 ms                                                                | 25.7 ms: 1.02x faster                                               |
| genshi_xml      | 61.8 ms                                                                | 62.6 ms: 1.01x slower                                               |
| mako            | 9.87 ms                                                                | 10.2 ms: 1.03x slower                                               |
| django_template | 37.1 ms                                                                | 40.5 ms: 1.09x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python         | 316 us                                                                 | 294 us: 1.08x faster                                                |
| scimark_monte_carlo        | 64.5 ms                                                                | 61.7 ms: 1.05x faster                                               |
| go                         | 133 ms                                                                 | 129 ms: 1.03x faster                                                |
| logging_silent             | 109 ns                                                                 | 106 ns: 1.02x faster                                                |
| genshi_text                | 26.3 ms                                                                | 25.7 ms: 1.02x faster                                               |
| scimark_lu                 | 115 ms                                                                 | 113 ms: 1.02x faster                                                |
| async_tree_io_tg           | 977 ms                                                                 | 959 ms: 1.02x faster                                                |
| xml_etree_parse            | 149 ms                                                                 | 146 ms: 1.02x faster                                                |
| regex_effbot               | 3.77 ms                                                                | 3.71 ms: 1.02x faster                                               |
| float                      | 76.1 ms                                                                | 75.0 ms: 1.01x faster                                               |
| typing_runtime_protocols   | 169 us                                                                 | 167 us: 1.01x faster                                                |
| regex_dna                  | 217 ms                                                                 | 215 ms: 1.01x faster                                                |
| scimark_fft                | 323 ms                                                                 | 321 ms: 1.01x faster                                                |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x faster                                                |
| create_gc_cycles           | 2.67 ms                                                                | 2.66 ms: 1.00x faster                                               |
| json_loads                 | 26.6 us                                                                | 26.7 us: 1.00x slower                                               |
| bpe_tokeniser              | 4.44 sec                                                               | 4.46 sec: 1.00x slower                                              |
| asyncio_websockets         | 554 ms                                                                 | 557 ms: 1.01x slower                                                |
| python_startup_no_site     | 7.05 ms                                                                | 7.11 ms: 1.01x slower                                               |
| json_dumps                 | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                               |
| tomli_loads                | 1.92 sec                                                               | 1.94 sec: 1.01x slower                                              |
| python_startup             | 11.8 ms                                                                | 11.9 ms: 1.01x slower                                               |
| genshi_xml                 | 61.8 ms                                                                | 62.6 ms: 1.01x slower                                               |
| deepcopy_memo              | 29.3 us                                                                | 29.7 us: 1.01x slower                                               |
| scimark_sparse_mat_mult    | 4.60 ms                                                                | 4.66 ms: 1.01x slower                                               |
| async_generators           | 460 ms                                                                 | 467 ms: 1.02x slower                                                |
| fannkuch                   | 376 ms                                                                 | 384 ms: 1.02x slower                                                |
| spectral_norm              | 116 ms                                                                 | 118 ms: 1.02x slower                                                |
| pathlib                    | 16.2 ms                                                                | 16.6 ms: 1.02x slower                                               |
| coverage                   | 84.4 ms                                                                | 86.4 ms: 1.02x slower                                               |
| comprehensions             | 17.0 us                                                                | 17.4 us: 1.02x slower                                               |
| scimark_sor                | 119 ms                                                                 | 122 ms: 1.03x slower                                                |
| 2to3                       | 279 ms                                                                 | 286 ms: 1.03x slower                                                |
| deepcopy                   | 269 us                                                                 | 277 us: 1.03x slower                                                |
| generators                 | 35.5 ms                                                                | 36.6 ms: 1.03x slower                                               |
| mako                       | 9.87 ms                                                                | 10.2 ms: 1.03x slower                                               |
| async_tree_none            | 336 ms                                                                 | 347 ms: 1.03x slower                                                |
| async_tree_cpu_io_mixed    | 577 ms                                                                 | 599 ms: 1.04x slower                                                |
| gc_traversal               | 4.55 ms                                                                | 4.74 ms: 1.04x slower                                               |
| sqlglot_normalize          | 115 ms                                                                 | 120 ms: 1.04x slower                                                |
| unpickle_pure_python       | 216 us                                                                 | 226 us: 1.04x slower                                                |
| hexiom                     | 7.13 ms                                                                | 7.44 ms: 1.04x slower                                               |
| async_tree_memoization     | 416 ms                                                                 | 434 ms: 1.05x slower                                                |
| thrift                     | 789 us                                                                 | 825 us: 1.05x slower                                                |
| regex_v8                   | 24.7 ms                                                                | 25.8 ms: 1.05x slower                                               |
| raytrace                   | 283 ms                                                                 | 296 ms: 1.05x slower                                                |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 589 ms: 1.05x slower                                                |
| mdp                        | 2.57 sec                                                               | 2.69 sec: 1.05x slower                                              |
| async_tree_none_tg         | 322 ms                                                                 | 338 ms: 1.05x slower                                                |
| deepcopy_reduce            | 2.77 us                                                                | 2.91 us: 1.05x slower                                               |
| html5lib                   | 65.2 ms                                                                | 68.6 ms: 1.05x slower                                               |
| regex_compile              | 139 ms                                                                 | 146 ms: 1.05x slower                                                |
| dulwich_log                | 66.4 ms                                                                | 70.0 ms: 1.06x slower                                               |
| sympy_expand               | 503 ms                                                                 | 533 ms: 1.06x slower                                                |
| xml_etree_generate         | 78.4 ms                                                                | 83.3 ms: 1.06x slower                                               |
| bench_mp_pool              | 83.7 ms                                                                | 89.0 ms: 1.06x slower                                               |
| async_tree_memoization_tg  | 380 ms                                                                 | 405 ms: 1.07x slower                                                |
| sqlglot_parse              | 1.34 ms                                                                | 1.43 ms: 1.07x slower                                               |
| sqlglot_transpile          | 1.71 ms                                                                | 1.85 ms: 1.08x slower                                               |
| xml_etree_process          | 55.3 ms                                                                | 60.1 ms: 1.09x slower                                               |
| django_template            | 37.1 ms                                                                | 40.5 ms: 1.09x slower                                               |
| sympy_str                  | 306 ms                                                                 | 334 ms: 1.09x slower                                                |
| async_tree_io              | 855 ms                                                                 | 941 ms: 1.10x slower                                                |
| pycparser                  | 1.15 sec                                                               | 1.27 sec: 1.10x slower                                              |
| bench_thread_pool          | 877 us                                                                 | 969 us: 1.10x slower                                                |
| sqlglot_optimize           | 60.1 ms                                                                | 66.7 ms: 1.11x slower                                               |
| coroutines                 | 23.1 ms                                                                | 26.4 ms: 1.14x slower                                               |
| sphinx                     | 1.17 sec                                                               | 1.35 sec: 1.15x slower                                              |
| sympy_integrate            | 23.6 ms                                                                | 27.3 ms: 1.16x slower                                               |
| sympy_sum                  | 177 ms                                                                 | 206 ms: 1.17x slower                                                |
| docutils                   | 2.91 sec                                                               | 3.40 sec: 1.17x slower                                              |
| richards                   | 41.8 ms                                                                | 48.8 ms: 1.17x slower                                               |
| tornado_http               | 94.6 ms                                                                | 112 ms: 1.18x slower                                                |
| sqlalchemy_declarative     | 147 ms                                                                 | 175 ms: 1.19x slower                                                |
| richards_super             | 45.5 ms                                                                | 54.7 ms: 1.20x slower                                               |
| logging_format             | 6.22 us                                                                | 7.57 us: 1.22x slower                                               |
| logging_simple             | 5.61 us                                                                | 7.01 us: 1.25x slower                                               |
| deltablue                  | 3.23 ms                                                                | 4.04 ms: 1.25x slower                                               |
| sqlalchemy_imperative      | 17.8 ms                                                                | 22.5 ms: 1.26x slower                                               |
| pylint                     | 325 ms                                                                 | 466 ms: 1.43x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.05x slower                                                        |

Benchmark hidden because not significant (11): crypto_pyaes, meteor_contest, nbody, chaos, xml_etree_iterparse, telco, json, pyflate, nqueens, pprint_safe_repr, pprint_pformat

- Geometric mean (including insignificant results): 1.047x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.04x