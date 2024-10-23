# Results vs. base

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: d0d3a27
- commit date: 2024-10-23
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 278 ms                                                                 | 288 ms: 1.04x slower                                                    |
| docutils       | 2.95 sec                                                               | 3.41 sec: 1.15x slower                                                  |
| html5lib       | 66.2 ms                                                                | 70.3 ms: 1.06x slower                                                   |
| sphinx         | 1.18 sec                                                               | 1.36 sec: 1.16x slower                                                  |
| tornado_http   | 94.5 ms                                                                | 112 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 974 ms                                                                 | 956 ms: 1.02x faster                                                    |
| asyncio_websockets         | 553 ms                                                                 | 558 ms: 1.01x slower                                                    |
| async_generators           | 456 ms                                                                 | 468 ms: 1.03x slower                                                    |
| async_tree_none_tg         | 320 ms                                                                 | 331 ms: 1.03x slower                                                    |
| async_tree_none            | 336 ms                                                                 | 350 ms: 1.04x slower                                                    |
| async_tree_memoization     | 416 ms                                                                 | 434 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed    | 570 ms                                                                 | 596 ms: 1.05x slower                                                    |
| async_tree_cpu_io_mixed_tg | 556 ms                                                                 | 584 ms: 1.05x slower                                                    |
| async_tree_memoization_tg  | 378 ms                                                                 | 408 ms: 1.08x slower                                                    |
| async_tree_io              | 852 ms                                                                 | 940 ms: 1.10x slower                                                    |
| coroutines                 | 23.3 ms                                                                | 26.6 ms: 1.14x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.05x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 82.5 ms                                                                | 81.2 ms: 1.02x faster                                                   |
| float          | 76.3 ms                                                                | 75.5 ms: 1.01x faster                                                   |
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                 | 223 ms: 1.01x slower                                                    |
| regex_v8       | 25.1 ms                                                                | 26.1 ms: 1.04x slower                                                   |
| regex_effbot   | 3.76 ms                                                                | 3.94 ms: 1.05x slower                                                   |
| regex_compile  | 137 ms                                                                 | 147 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 316 us                                                                 | 296 us: 1.07x faster                                                    |
| json_dumps           | 11.2 ms                                                                | 11.0 ms: 1.02x faster                                                   |
| json_loads           | 27.0 us                                                                | 26.7 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 100 ms                                                                 | 99.4 ms: 1.01x faster                                                   |
| tomli_loads          | 1.90 sec                                                               | 1.95 sec: 1.03x slower                                                  |
| unpickle_pure_python | 215 us                                                                 | 226 us: 1.05x slower                                                    |
| xml_etree_generate   | 78.6 ms                                                                | 82.8 ms: 1.05x slower                                                   |
| xml_etree_process    | 55.4 ms                                                                | 59.8 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                                | 11.9 ms: 1.00x slower                                                   |
| python_startup_no_site | 7.12 ms                                                                | 7.22 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 10.2 ms                                                                | 10.5 ms: 1.03x slower                                                   |
| genshi_text     | 25.6 ms                                                                | 26.6 ms: 1.04x slower                                                   |
| genshi_xml      | 60.1 ms                                                                | 62.8 ms: 1.05x slower                                                   |
| django_template | 36.2 ms                                                                | 40.5 ms: 1.12x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.06x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python         | 316 us                                                                 | 296 us: 1.07x faster                                                    |
| scimark_monte_carlo        | 64.5 ms                                                                | 62.3 ms: 1.04x faster                                                   |
| go                         | 132 ms                                                                 | 129 ms: 1.03x faster                                                    |
| json_dumps                 | 11.2 ms                                                                | 11.0 ms: 1.02x faster                                                   |
| async_tree_io_tg           | 974 ms                                                                 | 956 ms: 1.02x faster                                                    |
| nbody                      | 82.5 ms                                                                | 81.2 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 725 ms                                                                 | 715 ms: 1.01x faster                                                    |
| float                      | 76.3 ms                                                                | 75.5 ms: 1.01x faster                                                   |
| json_loads                 | 27.0 us                                                                | 26.7 us: 1.01x faster                                                   |
| xml_etree_iterparse        | 100 ms                                                                 | 99.4 ms: 1.01x faster                                                   |
| scimark_fft                | 321 ms                                                                 | 319 ms: 1.01x faster                                                    |
| fannkuch                   | 380 ms                                                                 | 378 ms: 1.01x faster                                                    |
| create_gc_cycles           | 2.70 ms                                                                | 2.69 ms: 1.00x faster                                                   |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x slower                                                    |
| python_startup             | 11.9 ms                                                                | 11.9 ms: 1.00x slower                                                   |
| scimark_sparse_mat_mult    | 4.63 ms                                                                | 4.66 ms: 1.01x slower                                                   |
| gc_traversal               | 4.81 ms                                                                | 4.85 ms: 1.01x slower                                                   |
| regex_dna                  | 221 ms                                                                 | 223 ms: 1.01x slower                                                    |
| asyncio_websockets         | 553 ms                                                                 | 558 ms: 1.01x slower                                                    |
| scimark_sor                | 119 ms                                                                 | 120 ms: 1.01x slower                                                    |
| scimark_lu                 | 113 ms                                                                 | 114 ms: 1.01x slower                                                    |
| python_startup_no_site     | 7.12 ms                                                                | 7.22 ms: 1.01x slower                                                   |
| pathlib                    | 16.0 ms                                                                | 16.4 ms: 1.02x slower                                                   |
| async_generators           | 456 ms                                                                 | 468 ms: 1.03x slower                                                    |
| pyflate                    | 455 ms                                                                 | 467 ms: 1.03x slower                                                    |
| logging_silent             | 105 ns                                                                 | 108 ns: 1.03x slower                                                    |
| tomli_loads                | 1.90 sec                                                               | 1.95 sec: 1.03x slower                                                  |
| mako                       | 10.2 ms                                                                | 10.5 ms: 1.03x slower                                                   |
| dulwich_log                | 66.4 ms                                                                | 68.6 ms: 1.03x slower                                                   |
| async_tree_none_tg         | 320 ms                                                                 | 331 ms: 1.03x slower                                                    |
| deepcopy                   | 267 us                                                                 | 276 us: 1.03x slower                                                    |
| deepcopy_memo              | 29.1 us                                                                | 30.1 us: 1.04x slower                                                   |
| mdp                        | 2.56 sec                                                               | 2.65 sec: 1.04x slower                                                  |
| 2to3                       | 278 ms                                                                 | 288 ms: 1.04x slower                                                    |
| coverage                   | 83.8 ms                                                                | 86.9 ms: 1.04x slower                                                   |
| genshi_text                | 25.6 ms                                                                | 26.6 ms: 1.04x slower                                                   |
| generators                 | 35.2 ms                                                                | 36.5 ms: 1.04x slower                                                   |
| regex_v8                   | 25.1 ms                                                                | 26.1 ms: 1.04x slower                                                   |
| async_tree_none            | 336 ms                                                                 | 350 ms: 1.04x slower                                                    |
| raytrace                   | 284 ms                                                                 | 295 ms: 1.04x slower                                                    |
| async_tree_memoization     | 416 ms                                                                 | 434 ms: 1.04x slower                                                    |
| comprehensions             | 17.1 us                                                                | 17.8 us: 1.04x slower                                                   |
| genshi_xml                 | 60.1 ms                                                                | 62.8 ms: 1.05x slower                                                   |
| async_tree_cpu_io_mixed    | 570 ms                                                                 | 596 ms: 1.05x slower                                                    |
| regex_effbot               | 3.76 ms                                                                | 3.94 ms: 1.05x slower                                                   |
| thrift                     | 787 us                                                                 | 826 us: 1.05x slower                                                    |
| async_tree_cpu_io_mixed_tg | 556 ms                                                                 | 584 ms: 1.05x slower                                                    |
| unpickle_pure_python       | 215 us                                                                 | 226 us: 1.05x slower                                                    |
| xml_etree_generate         | 78.6 ms                                                                | 82.8 ms: 1.05x slower                                                   |
| html5lib                   | 66.2 ms                                                                | 70.3 ms: 1.06x slower                                                   |
| sqlglot_normalize          | 113 ms                                                                 | 121 ms: 1.06x slower                                                    |
| bench_mp_pool              | 84.4 ms                                                                | 89.9 ms: 1.06x slower                                                   |
| regex_compile              | 137 ms                                                                 | 147 ms: 1.07x slower                                                    |
| sympy_expand               | 502 ms                                                                 | 536 ms: 1.07x slower                                                    |
| deepcopy_reduce            | 2.72 us                                                                | 2.91 us: 1.07x slower                                                   |
| hexiom                     | 6.98 ms                                                                | 7.48 ms: 1.07x slower                                                   |
| async_tree_memoization_tg  | 378 ms                                                                 | 408 ms: 1.08x slower                                                    |
| xml_etree_process          | 55.4 ms                                                                | 59.8 ms: 1.08x slower                                                   |
| sqlglot_parse              | 1.33 ms                                                                | 1.44 ms: 1.08x slower                                                   |
| bench_thread_pool          | 881 us                                                                 | 963 us: 1.09x slower                                                    |
| sqlglot_transpile          | 1.69 ms                                                                | 1.85 ms: 1.09x slower                                                   |
| sympy_str                  | 303 ms                                                                 | 333 ms: 1.10x slower                                                    |
| async_tree_io              | 852 ms                                                                 | 940 ms: 1.10x slower                                                    |
| django_template            | 36.2 ms                                                                | 40.5 ms: 1.12x slower                                                   |
| sqlglot_optimize           | 59.6 ms                                                                | 67.2 ms: 1.13x slower                                                   |
| coroutines                 | 23.3 ms                                                                | 26.6 ms: 1.14x slower                                                   |
| docutils                   | 2.95 sec                                                               | 3.41 sec: 1.15x slower                                                  |
| sphinx                     | 1.18 sec                                                               | 1.36 sec: 1.16x slower                                                  |
| pycparser                  | 1.15 sec                                                               | 1.34 sec: 1.16x slower                                                  |
| sympy_integrate            | 23.4 ms                                                                | 27.6 ms: 1.18x slower                                                   |
| richards                   | 42.4 ms                                                                | 49.9 ms: 1.18x slower                                                   |
| sympy_sum                  | 176 ms                                                                 | 208 ms: 1.18x slower                                                    |
| tornado_http               | 94.5 ms                                                                | 112 ms: 1.18x slower                                                    |
| logging_format             | 6.15 us                                                                | 7.43 us: 1.21x slower                                                   |
| richards_super             | 45.4 ms                                                                | 55.2 ms: 1.22x slower                                                   |
| logging_simple             | 5.54 us                                                                | 6.90 us: 1.25x slower                                                   |
| deltablue                  | 3.23 ms                                                                | 4.03 ms: 1.25x slower                                                   |
| pylint                     | 356 ms                                                                 | 468 ms: 1.32x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.05x slower                                                            |

Benchmark hidden because not significant (11): xml_etree_parse, spectral_norm, telco, pprint_pformat, crypto_pyaes, json, nqueens, meteor_contest, chaos, typing_runtime_protocols, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.04x