# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b2
- machine: linux-aarch64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------:|
| 2to3           | 360 ms                                                                                                     | 305 ms: 1.18x faster                                                                                   |
| chameleon      | 9.18 ms                                                                                                    | 8.95 ms: 1.03x faster                                                                                  |
| docutils       | 3.52 sec                                                                                                   | 3.10 sec: 1.14x faster                                                                                 |
| html5lib       | 71.7 ms                                                                                                    | 66.1 ms: 1.09x faster                                                                                  |
| tornado_http   | 139 ms                                                                                                     | 128 ms: 1.08x faster                                                                                   |
| Geometric mean | (ref)                                                                                                      | 1.10x faster                                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 806 ms                                                                                                     | 763 ms: 1.06x faster                                                                                   |
| async_tree_memoization     | 671 ms                                                                                                     | 645 ms: 1.04x faster                                                                                   |
| async_tree_cpu_io_mixed    | 818 ms                                                                                                     | 791 ms: 1.03x faster                                                                                   |
| async_tree_none            | 508 ms                                                                                                     | 492 ms: 1.03x faster                                                                                   |
| async_tree_io_tg           | 1.23 sec                                                                                                   | 1.27 sec: 1.04x slower                                                                                 |
| Geometric mean             | (ref)                                                                                                      | 1.02x faster                                                                                           |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------:|
| nbody          | 116 ms                                                                                                     | 114 ms: 1.01x faster                                                                                   |
| float          | 88.7 ms                                                                                                    | 91.4 ms: 1.03x slower                                                                                  |
| Geometric mean | (ref)                                                                                                      | 1.00x slower                                                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------:|
| regex_compile  | 175 ms                                                                                                     | 128 ms: 1.37x faster                                                                                   |
| regex_v8       | 30.4 ms                                                                                                    | 31.1 ms: 1.02x slower                                                                                  |
| regex_effbot   | 4.86 ms                                                                                                    | 4.98 ms: 1.03x slower                                                                                  |
| regex_dna      | 247 ms                                                                                                     | 259 ms: 1.05x slower                                                                                   |
| Geometric mean | (ref)                                                                                                      | 1.06x faster                                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------|:----------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------:|
| pickle_pure_python   | 398 us                                                                                                     | 359 us: 1.11x faster                                                                                   |
| unpickle_pure_python | 278 us                                                                                                     | 251 us: 1.11x faster                                                                                   |
| tomli_loads          | 2.64 sec                                                                                                   | 2.57 sec: 1.03x faster                                                                                 |
| json_dumps           | 13.3 ms                                                                                                    | 13.1 ms: 1.02x faster                                                                                  |
| xml_etree_iterparse  | 148 ms                                                                                                     | 147 ms: 1.01x faster                                                                                   |
| pickle_list          | 5.30 us                                                                                                    | 5.27 us: 1.01x faster                                                                                  |
| Geometric mean       | (ref)                                                                                                      | 1.02x faster                                                                                           |

Benchmark hidden because not significant (8): pickle, unpickle_list, xml_etree_generate, json_loads, pickle_dict, unpickle, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|------------------------|:----------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 10.9 ms                                                                                                    | 8.60 ms: 1.26x faster                                                                                  |
| python_startup         | 15.3 ms                                                                                                    | 13.0 ms: 1.18x faster                                                                                  |
| Geometric mean         | (ref)                                                                                                      | 1.22x faster                                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|-----------------|:----------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 83.4 ms                                                                                                    | 60.4 ms: 1.38x faster                                                                                  |
| genshi_text     | 35.4 ms                                                                                                    | 27.4 ms: 1.29x faster                                                                                  |
| django_template | 49.6 ms                                                                                                    | 42.3 ms: 1.17x faster                                                                                  |
| mako            | 13.0 ms                                                                                                    | 13.2 ms: 1.01x slower                                                                                  |
| Geometric mean  | (ref)                                                                                                      | 1.20x faster                                                                                           |

All benchmarks:
===============

| Benchmark                  | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------:|
| genshi_xml                 | 83.4 ms                                                                                                    | 60.4 ms: 1.38x faster                                                                                  |
| regex_compile              | 175 ms                                                                                                     | 128 ms: 1.37x faster                                                                                   |
| scimark_lu                 | 183 ms                                                                                                     | 141 ms: 1.29x faster                                                                                   |
| genshi_text                | 35.4 ms                                                                                                    | 27.4 ms: 1.29x faster                                                                                  |
| chaos                      | 87.1 ms                                                                                                    | 68.3 ms: 1.28x faster                                                                                  |
| sympy_sum                  | 183 ms                                                                                                     | 144 ms: 1.27x faster                                                                                   |
| python_startup_no_site     | 10.9 ms                                                                                                    | 8.60 ms: 1.26x faster                                                                                  |
| hexiom                     | 8.89 ms                                                                                                    | 7.08 ms: 1.26x faster                                                                                  |
| pylint                     | 414 ms                                                                                                     | 337 ms: 1.23x faster                                                                                   |
| sympy_integrate            | 25.5 ms                                                                                                    | 20.9 ms: 1.22x faster                                                                                  |
| dulwich_log                | 71.0 ms                                                                                                    | 58.5 ms: 1.21x faster                                                                                  |
| mypy2                      | 929 ms                                                                                                     | 767 ms: 1.21x faster                                                                                   |
| sympy_str                  | 321 ms                                                                                                     | 265 ms: 1.21x faster                                                                                   |
| pprint_pformat             | 2.31 sec                                                                                                   | 1.93 sec: 1.20x faster                                                                                 |
| pprint_safe_repr           | 1.11 sec                                                                                                   | 933 ms: 1.19x faster                                                                                   |
| nqueens                    | 117 ms                                                                                                     | 98.9 ms: 1.18x faster                                                                                  |
| 2to3                       | 360 ms                                                                                                     | 305 ms: 1.18x faster                                                                                   |
| deltablue                  | 4.58 ms                                                                                                    | 3.88 ms: 1.18x faster                                                                                  |
| python_startup             | 15.3 ms                                                                                                    | 13.0 ms: 1.18x faster                                                                                  |
| sympy_expand               | 538 ms                                                                                                     | 457 ms: 1.18x faster                                                                                   |
| bench_mp_pool              | 8.24 ms                                                                                                    | 7.03 ms: 1.17x faster                                                                                  |
| django_template            | 49.6 ms                                                                                                    | 42.3 ms: 1.17x faster                                                                                  |
| sqlglot_transpile          | 2.00 ms                                                                                                    | 1.71 ms: 1.17x faster                                                                                  |
| deepcopy_reduce            | 4.68 us                                                                                                    | 4.04 us: 1.16x faster                                                                                  |
| gunicorn                   | 1.36 ms                                                                                                    | 1.19 ms: 1.15x faster                                                                                  |
| docutils                   | 3.52 sec                                                                                                   | 3.10 sec: 1.14x faster                                                                                 |
| comprehensions             | 23.2 us                                                                                                    | 20.5 us: 1.13x faster                                                                                  |
| deepcopy                   | 502 us                                                                                                     | 448 us: 1.12x faster                                                                                   |
| sqlglot_normalize          | 144 ms                                                                                                     | 129 ms: 1.12x faster                                                                                   |
| go                         | 180 ms                                                                                                     | 161 ms: 1.12x faster                                                                                   |
| sqlglot_optimize           | 69.8 ms                                                                                                    | 62.6 ms: 1.11x faster                                                                                  |
| pickle_pure_python         | 398 us                                                                                                     | 359 us: 1.11x faster                                                                                   |
| sqlglot_parse              | 1.58 ms                                                                                                    | 1.42 ms: 1.11x faster                                                                                  |
| pycparser                  | 1.35 sec                                                                                                   | 1.22 sec: 1.11x faster                                                                                 |
| unpickle_pure_python       | 278 us                                                                                                     | 251 us: 1.11x faster                                                                                   |
| flaskblogging              | 5.16 ms                                                                                                    | 4.70 ms: 1.10x faster                                                                                  |
| scimark_sor                | 174 ms                                                                                                     | 159 ms: 1.09x faster                                                                                   |
| crypto_pyaes               | 89.1 ms                                                                                                    | 82.0 ms: 1.09x faster                                                                                  |
| aiohttp                    | 1.28 ms                                                                                                    | 1.18 ms: 1.09x faster                                                                                  |
| html5lib                   | 71.7 ms                                                                                                    | 66.1 ms: 1.09x faster                                                                                  |
| tornado_http               | 139 ms                                                                                                     | 128 ms: 1.08x faster                                                                                   |
| raytrace                   | 321 ms                                                                                                     | 297 ms: 1.08x faster                                                                                   |
| scimark_monte_carlo        | 89.0 ms                                                                                                    | 82.3 ms: 1.08x faster                                                                                  |
| pyflate                    | 596 ms                                                                                                     | 557 ms: 1.07x faster                                                                                   |
| typing_runtime_protocols   | 207 us                                                                                                     | 193 us: 1.07x faster                                                                                   |
| generators                 | 39.6 ms                                                                                                    | 37.1 ms: 1.07x faster                                                                                  |
| dask                       | 393 ms                                                                                                     | 370 ms: 1.06x faster                                                                                   |
| scimark_sparse_mat_mult    | 6.94 ms                                                                                                    | 6.55 ms: 1.06x faster                                                                                  |
| asyncio_tcp                | 618 ms                                                                                                     | 584 ms: 1.06x faster                                                                                   |
| async_tree_cpu_io_mixed_tg | 806 ms                                                                                                     | 763 ms: 1.06x faster                                                                                   |
| logging_silent             | 141 ns                                                                                                     | 133 ns: 1.06x faster                                                                                   |
| spectral_norm              | 149 ms                                                                                                     | 141 ms: 1.05x faster                                                                                   |
| bench_thread_pool          | 1.32 ms                                                                                                    | 1.26 ms: 1.05x faster                                                                                  |
| async_generators           | 508 ms                                                                                                     | 488 ms: 1.04x faster                                                                                   |
| async_tree_memoization     | 671 ms                                                                                                     | 645 ms: 1.04x faster                                                                                   |
| meteor_contest             | 118 ms                                                                                                     | 113 ms: 1.04x faster                                                                                   |
| async_tree_cpu_io_mixed    | 818 ms                                                                                                     | 791 ms: 1.03x faster                                                                                   |
| async_tree_none            | 508 ms                                                                                                     | 492 ms: 1.03x faster                                                                                   |
| mdp                        | 3.44 sec                                                                                                   | 3.33 sec: 1.03x faster                                                                                 |
| scimark_fft                | 459 ms                                                                                                     | 445 ms: 1.03x faster                                                                                   |
| logging_format             | 8.05 us                                                                                                    | 7.82 us: 1.03x faster                                                                                  |
| fannkuch                   | 463 ms                                                                                                     | 451 ms: 1.03x faster                                                                                   |
| chameleon                  | 9.18 ms                                                                                                    | 8.95 ms: 1.03x faster                                                                                  |
| tomli_loads                | 2.64 sec                                                                                                   | 2.57 sec: 1.03x faster                                                                                 |
| bpe_tokeniser              | 5.97 sec                                                                                                   | 5.83 sec: 1.03x faster                                                                                 |
| pathlib                    | 23.2 ms                                                                                                    | 22.8 ms: 1.02x faster                                                                                  |
| richards_super             | 63.4 ms                                                                                                    | 62.3 ms: 1.02x faster                                                                                  |
| asyncio_tcp_ssl            | 2.25 sec                                                                                                   | 2.21 sec: 1.02x faster                                                                                 |
| json_dumps                 | 13.3 ms                                                                                                    | 13.1 ms: 1.02x faster                                                                                  |
| nbody                      | 116 ms                                                                                                     | 114 ms: 1.01x faster                                                                                   |
| xml_etree_iterparse        | 148 ms                                                                                                     | 147 ms: 1.01x faster                                                                                   |
| pickle_list                | 5.30 us                                                                                                    | 5.27 us: 1.01x faster                                                                                  |
| mako                       | 13.0 ms                                                                                                    | 13.2 ms: 1.01x slower                                                                                  |
| gc_traversal               | 5.08 ms                                                                                                    | 5.17 ms: 1.02x slower                                                                                  |
| deepcopy_memo              | 49.7 us                                                                                                    | 50.8 us: 1.02x slower                                                                                  |
| regex_v8                   | 30.4 ms                                                                                                    | 31.1 ms: 1.02x slower                                                                                  |
| regex_effbot               | 4.86 ms                                                                                                    | 4.98 ms: 1.03x slower                                                                                  |
| float                      | 88.7 ms                                                                                                    | 91.4 ms: 1.03x slower                                                                                  |
| sqlite_synth               | 3.78 us                                                                                                    | 3.90 us: 1.03x slower                                                                                  |
| async_tree_io_tg           | 1.23 sec                                                                                                   | 1.27 sec: 1.04x slower                                                                                 |
| regex_dna                  | 247 ms                                                                                                     | 259 ms: 1.05x slower                                                                                   |
| Geometric mean             | (ref)                                                                                                      | 1.08x faster                                                                                           |

Benchmark hidden because not significant (21): async_tree_memoization_tg, async_tree_io, async_tree_none_tg, create_gc_cycles, json, logging_simple, telco, pickle, unpickle_list, richards, thrift, xml_etree_generate, asyncio_websockets, pidigits, json_loads, pickle_dict, coverage, unpickle, coroutines, xml_etree_process, xml_etree_parse

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.92x