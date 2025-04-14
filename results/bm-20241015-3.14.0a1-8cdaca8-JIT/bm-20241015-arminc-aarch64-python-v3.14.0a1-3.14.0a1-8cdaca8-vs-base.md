# Results vs. base

- fork: python
- ref: v3.14.0a1
- machine: linux-aarch64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.111x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                                                                 | 382 ms: 1.30x slower                                                                                       |
| docutils       | 3.01 sec                                                                                               | 3.61 sec: 1.20x slower                                                                                     |
| html5lib       | 64.6 ms                                                                                                | 71.8 ms: 1.11x slower                                                                                      |
| sphinx         | 1.18 sec                                                                                               | 1.46 sec: 1.24x slower                                                                                     |
| tornado_http   | 125 ms                                                                                                 | 147 ms: 1.18x slower                                                                                       |
| Geometric mean | (ref)                                                                                                  | 1.20x slower                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 743 ms                                                                                                 | 759 ms: 1.02x slower                                                                                       |
| async_tree_cpu_io_mixed_tg | 724 ms                                                                                                 | 742 ms: 1.02x slower                                                                                       |
| asyncio_tcp_ssl            | 2.21 sec                                                                                               | 2.27 sec: 1.03x slower                                                                                     |
| async_tree_io_tg           | 1.21 sec                                                                                               | 1.25 sec: 1.03x slower                                                                                     |
| async_tree_none            | 438 ms                                                                                                 | 463 ms: 1.06x slower                                                                                       |
| async_generators           | 479 ms                                                                                                 | 507 ms: 1.06x slower                                                                                       |
| async_tree_memoization     | 563 ms                                                                                                 | 605 ms: 1.07x slower                                                                                       |
| asyncio_tcp                | 554 ms                                                                                                 | 630 ms: 1.14x slower                                                                                       |
| Geometric mean             | (ref)                                                                                                  | 1.04x slower                                                                                               |

Benchmark hidden because not significant (5): async_tree_io, coroutines, async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| nbody          | 114 ms                                                                                                 | 116 ms: 1.02x slower                                                                                       |
| float          | 95.4 ms                                                                                                | 97.2 ms: 1.02x slower                                                                                      |
| Geometric mean | (ref)                                                                                                  | 1.01x slower                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                                                                | 31.6 ms: 1.01x slower                                                                                      |
| regex_compile  | 125 ms                                                                                                 | 179 ms: 1.43x slower                                                                                       |
| Geometric mean | (ref)                                                                                                  | 1.10x slower                                                                                               |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                                                                 | 186 ms: 1.03x faster                                                                                       |
| pickle_list          | 5.22 us                                                                                                | 5.12 us: 1.02x faster                                                                                      |
| unpickle_list        | 6.60 us                                                                                                | 6.52 us: 1.01x faster                                                                                      |
| tomli_loads          | 2.63 sec                                                                                               | 2.65 sec: 1.01x slower                                                                                     |
| json_loads           | 31.2 us                                                                                                | 31.7 us: 1.02x slower                                                                                      |
| json_dumps           | 14.1 ms                                                                                                | 14.4 ms: 1.02x slower                                                                                      |
| unpickle_pure_python | 255 us                                                                                                 | 268 us: 1.05x slower                                                                                       |
| pickle_pure_python   | 365 us                                                                                                 | 389 us: 1.06x slower                                                                                       |
| Geometric mean       | (ref)                                                                                                  | 1.00x slower                                                                                               |

Benchmark hidden because not significant (6): xml_etree_generate, pickle, unpickle, xml_etree_process, pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|------------------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| python_startup         | 14.5 ms                                                                                                | 14.7 ms: 1.01x slower                                                                                      |
| python_startup_no_site | 8.63 ms                                                                                                | 8.79 ms: 1.02x slower                                                                                      |
| Geometric mean         | (ref)                                                                                                  | 1.01x slower                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|-----------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| mako            | 13.7 ms                                                                                                | 13.2 ms: 1.03x faster                                                                                      |
| genshi_text     | 27.5 ms                                                                                                | 34.2 ms: 1.24x slower                                                                                      |
| django_template | 42.1 ms                                                                                                | 52.4 ms: 1.25x slower                                                                                      |
| genshi_xml      | 61.6 ms                                                                                                | 84.1 ms: 1.37x slower                                                                                      |
| Geometric mean  | (ref)                                                                                                  | 1.20x slower                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json | results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json |
|----------------------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 4.94 sec                                                                                               | 1.45 sec: 3.41x faster                                                                                     |
| mako                       | 13.7 ms                                                                                                | 13.2 ms: 1.03x faster                                                                                      |
| xml_etree_parse            | 191 ms                                                                                                 | 186 ms: 1.03x faster                                                                                       |
| scimark_sor                | 157 ms                                                                                                 | 154 ms: 1.02x faster                                                                                       |
| pickle_list                | 5.22 us                                                                                                | 5.12 us: 1.02x faster                                                                                      |
| unpickle_list              | 6.60 us                                                                                                | 6.52 us: 1.01x faster                                                                                      |
| tomli_loads                | 2.63 sec                                                                                               | 2.65 sec: 1.01x slower                                                                                     |
| sqlite_synth               | 3.86 us                                                                                                | 3.89 us: 1.01x slower                                                                                      |
| python_startup             | 14.5 ms                                                                                                | 14.7 ms: 1.01x slower                                                                                      |
| regex_v8                   | 31.1 ms                                                                                                | 31.6 ms: 1.01x slower                                                                                      |
| pathlib                    | 21.2 ms                                                                                                | 21.6 ms: 1.02x slower                                                                                      |
| json_loads                 | 31.2 us                                                                                                | 31.7 us: 1.02x slower                                                                                      |
| json_dumps                 | 14.1 ms                                                                                                | 14.4 ms: 1.02x slower                                                                                      |
| nbody                      | 114 ms                                                                                                 | 116 ms: 1.02x slower                                                                                       |
| python_startup_no_site     | 8.63 ms                                                                                                | 8.79 ms: 1.02x slower                                                                                      |
| float                      | 95.4 ms                                                                                                | 97.2 ms: 1.02x slower                                                                                      |
| telco                      | 9.54 ms                                                                                                | 9.74 ms: 1.02x slower                                                                                      |
| async_tree_cpu_io_mixed    | 743 ms                                                                                                 | 759 ms: 1.02x slower                                                                                       |
| async_tree_cpu_io_mixed_tg | 724 ms                                                                                                 | 742 ms: 1.02x slower                                                                                       |
| deepcopy_memo              | 38.2 us                                                                                                | 39.2 us: 1.03x slower                                                                                      |
| asyncio_tcp_ssl            | 2.21 sec                                                                                               | 2.27 sec: 1.03x slower                                                                                     |
| thrift                     | 929 us                                                                                                 | 956 us: 1.03x slower                                                                                       |
| async_tree_io_tg           | 1.21 sec                                                                                               | 1.25 sec: 1.03x slower                                                                                     |
| bpe_tokeniser              | 5.76 sec                                                                                               | 5.97 sec: 1.04x slower                                                                                     |
| coverage                   | 97.6 ms                                                                                                | 101 ms: 1.04x slower                                                                                       |
| json                       | 5.46 ms                                                                                                | 5.67 ms: 1.04x slower                                                                                      |
| mdp                        | 3.35 sec                                                                                               | 3.51 sec: 1.05x slower                                                                                     |
| unpickle_pure_python       | 255 us                                                                                                 | 268 us: 1.05x slower                                                                                       |
| scimark_fft                | 433 ms                                                                                                 | 454 ms: 1.05x slower                                                                                       |
| pyflate                    | 585 ms                                                                                                 | 615 ms: 1.05x slower                                                                                       |
| bench_thread_pool          | 1.30 ms                                                                                                | 1.37 ms: 1.05x slower                                                                                      |
| async_tree_none            | 438 ms                                                                                                 | 463 ms: 1.06x slower                                                                                       |
| async_generators           | 479 ms                                                                                                 | 507 ms: 1.06x slower                                                                                       |
| pickle_pure_python         | 365 us                                                                                                 | 389 us: 1.06x slower                                                                                       |
| scimark_monte_carlo        | 83.7 ms                                                                                                | 89.5 ms: 1.07x slower                                                                                      |
| fannkuch                   | 469 ms                                                                                                 | 503 ms: 1.07x slower                                                                                       |
| async_tree_memoization     | 563 ms                                                                                                 | 605 ms: 1.07x slower                                                                                       |
| logging_format             | 7.51 us                                                                                                | 8.08 us: 1.08x slower                                                                                      |
| spectral_norm              | 142 ms                                                                                                 | 155 ms: 1.09x slower                                                                                       |
| logging_simple             | 6.82 us                                                                                                | 7.45 us: 1.09x slower                                                                                      |
| scimark_sparse_mat_mult    | 6.46 ms                                                                                                | 7.16 ms: 1.11x slower                                                                                      |
| html5lib                   | 64.6 ms                                                                                                | 71.8 ms: 1.11x slower                                                                                      |
| meteor_contest             | 110 ms                                                                                                 | 123 ms: 1.12x slower                                                                                       |
| deepcopy_reduce            | 3.56 us                                                                                                | 3.98 us: 1.12x slower                                                                                      |
| crypto_pyaes               | 80.9 ms                                                                                                | 90.8 ms: 1.12x slower                                                                                      |
| typing_runtime_protocols   | 194 us                                                                                                 | 218 us: 1.12x slower                                                                                       |
| raytrace                   | 311 ms                                                                                                 | 349 ms: 1.12x slower                                                                                       |
| deepcopy                   | 333 us                                                                                                 | 377 us: 1.13x slower                                                                                       |
| scimark_lu                 | 133 ms                                                                                                 | 151 ms: 1.14x slower                                                                                       |
| asyncio_tcp                | 554 ms                                                                                                 | 630 ms: 1.14x slower                                                                                       |
| deltablue                  | 3.95 ms                                                                                                | 4.55 ms: 1.15x slower                                                                                      |
| tornado_http               | 125 ms                                                                                                 | 147 ms: 1.18x slower                                                                                       |
| richards_super             | 60.0 ms                                                                                                | 71.4 ms: 1.19x slower                                                                                      |
| comprehensions             | 20.6 us                                                                                                | 24.7 us: 1.20x slower                                                                                      |
| docutils                   | 3.01 sec                                                                                               | 3.61 sec: 1.20x slower                                                                                     |
| richards                   | 53.4 ms                                                                                                | 64.2 ms: 1.20x slower                                                                                      |
| sqlglot_parse              | 1.41 ms                                                                                                | 1.70 ms: 1.21x slower                                                                                      |
| chaos                      | 69.3 ms                                                                                                | 85.0 ms: 1.23x slower                                                                                      |
| sphinx                     | 1.18 sec                                                                                               | 1.46 sec: 1.24x slower                                                                                     |
| genshi_text                | 27.5 ms                                                                                                | 34.2 ms: 1.24x slower                                                                                      |
| sqlglot_normalize          | 126 ms                                                                                                 | 157 ms: 1.24x slower                                                                                       |
| django_template            | 42.1 ms                                                                                                | 52.4 ms: 1.25x slower                                                                                      |
| pycparser                  | 1.21 sec                                                                                               | 1.52 sec: 1.25x slower                                                                                     |
| sqlglot_transpile          | 1.75 ms                                                                                                | 2.20 ms: 1.26x slower                                                                                      |
| nqueens                    | 98.4 ms                                                                                                | 125 ms: 1.27x slower                                                                                       |
| sympy_expand               | 457 ms                                                                                                 | 594 ms: 1.30x slower                                                                                       |
| 2to3                       | 293 ms                                                                                                 | 382 ms: 1.30x slower                                                                                       |
| sqlglot_optimize           | 61.8 ms                                                                                                | 82.2 ms: 1.33x slower                                                                                      |
| pprint_safe_repr           | 909 ms                                                                                                 | 1.21 sec: 1.33x slower                                                                                     |
| go                         | 136 ms                                                                                                 | 184 ms: 1.35x slower                                                                                       |
| dulwich_log                | 57.0 ms                                                                                                | 77.6 ms: 1.36x slower                                                                                      |
| pprint_pformat             | 1.87 sec                                                                                               | 2.55 sec: 1.36x slower                                                                                     |
| genshi_xml                 | 61.6 ms                                                                                                | 84.1 ms: 1.37x slower                                                                                      |
| sympy_str                  | 261 ms                                                                                                 | 357 ms: 1.37x slower                                                                                       |
| pylint                     | 354 ms                                                                                                 | 494 ms: 1.40x slower                                                                                       |
| sympy_integrate            | 20.9 ms                                                                                                | 29.4 ms: 1.40x slower                                                                                      |
| regex_compile              | 125 ms                                                                                                 | 179 ms: 1.43x slower                                                                                       |
| hexiom                     | 6.97 ms                                                                                                | 10.3 ms: 1.48x slower                                                                                      |
| sympy_sum                  | 138 ms                                                                                                 | 215 ms: 1.55x slower                                                                                       |
| generators                 | 34.8 ms                                                                                                | 59.0 ms: 1.69x slower                                                                                      |
| unpack_sequence            | 57.4 ns                                                                                                | 146 ns: 2.55x slower                                                                                       |
| Geometric mean             | (ref)                                                                                                  | 1.11x slower                                                                                               |

Benchmark hidden because not significant (17): xml_etree_generate, pickle, gc_traversal, unpickle, xml_etree_process, create_gc_cycles, pickle_dict, regex_dna, async_tree_io, pidigits, coroutines, async_tree_memoization_tg, regex_effbot, asyncio_websockets, async_tree_none_tg, logging_silent, xml_etree_iterparse

- Geometric mean (including insignificant results): 1.111x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.06x