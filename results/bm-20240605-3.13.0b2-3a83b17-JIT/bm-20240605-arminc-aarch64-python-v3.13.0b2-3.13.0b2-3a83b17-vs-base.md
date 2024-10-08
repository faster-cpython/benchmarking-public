# Results vs. base

- fork: python
- ref: v3.13.0b2
- machine: linux-aarch64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                                                                 | 360 ms: 1.18x slower                                                                                       |
| chameleon      | 8.95 ms                                                                                                | 9.18 ms: 1.03x slower                                                                                      |
| docutils       | 3.10 sec                                                                                               | 3.52 sec: 1.14x slower                                                                                     |
| html5lib       | 66.1 ms                                                                                                | 71.7 ms: 1.09x slower                                                                                      |
| tornado_http   | 128 ms                                                                                                 | 139 ms: 1.08x slower                                                                                       |
| Geometric mean | (ref)                                                                                                  | 1.10x slower                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                                                               | 1.23 sec: 1.04x faster                                                                                     |
| async_tree_none            | 492 ms                                                                                                 | 508 ms: 1.03x slower                                                                                       |
| async_tree_cpu_io_mixed    | 791 ms                                                                                                 | 818 ms: 1.03x slower                                                                                       |
| async_tree_memoization     | 645 ms                                                                                                 | 671 ms: 1.04x slower                                                                                       |
| async_tree_cpu_io_mixed_tg | 763 ms                                                                                                 | 806 ms: 1.06x slower                                                                                       |
| Geometric mean             | (ref)                                                                                                  | 1.02x slower                                                                                               |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| float          | 91.4 ms                                                                                                | 88.7 ms: 1.03x faster                                                                                      |
| nbody          | 114 ms                                                                                                 | 116 ms: 1.01x slower                                                                                       |
| Geometric mean | (ref)                                                                                                  | 1.00x faster                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                                                                 | 247 ms: 1.05x faster                                                                                       |
| regex_effbot   | 4.98 ms                                                                                                | 4.86 ms: 1.03x faster                                                                                      |
| regex_v8       | 31.1 ms                                                                                                | 30.4 ms: 1.02x faster                                                                                      |
| regex_compile  | 128 ms                                                                                                 | 175 ms: 1.37x slower                                                                                       |
| Geometric mean | (ref)                                                                                                  | 1.06x slower                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| pickle_list          | 5.27 us                                                                                                | 5.30 us: 1.01x slower                                                                                      |
| xml_etree_iterparse  | 147 ms                                                                                                 | 148 ms: 1.01x slower                                                                                       |
| json_dumps           | 13.1 ms                                                                                                | 13.3 ms: 1.02x slower                                                                                      |
| tomli_loads          | 2.57 sec                                                                                               | 2.64 sec: 1.03x slower                                                                                     |
| unpickle_pure_python | 251 us                                                                                                 | 278 us: 1.11x slower                                                                                       |
| pickle_pure_python   | 359 us                                                                                                 | 398 us: 1.11x slower                                                                                       |
| Geometric mean       | (ref)                                                                                                  | 1.02x slower                                                                                               |

Benchmark hidden because not significant (8): xml_etree_parse, xml_etree_process, unpickle, pickle_dict, json_loads, xml_etree_generate, unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|------------------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                                                | 15.3 ms: 1.18x slower                                                                                      |
| python_startup_no_site | 8.60 ms                                                                                                | 10.9 ms: 1.26x slower                                                                                      |
| Geometric mean         | (ref)                                                                                                  | 1.22x slower                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|-----------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                                                                | 13.0 ms: 1.01x faster                                                                                      |
| django_template | 42.3 ms                                                                                                | 49.6 ms: 1.17x slower                                                                                      |
| genshi_text     | 27.4 ms                                                                                                | 35.4 ms: 1.29x slower                                                                                      |
| genshi_xml      | 60.4 ms                                                                                                | 83.4 ms: 1.38x slower                                                                                      |
| Geometric mean  | (ref)                                                                                                  | 1.20x slower                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------------|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| regex_dna                  | 259 ms                                                                                                 | 247 ms: 1.05x faster                                                                                       |
| async_tree_io_tg           | 1.27 sec                                                                                               | 1.23 sec: 1.04x faster                                                                                     |
| sqlite_synth               | 3.90 us                                                                                                | 3.78 us: 1.03x faster                                                                                      |
| float                      | 91.4 ms                                                                                                | 88.7 ms: 1.03x faster                                                                                      |
| regex_effbot               | 4.98 ms                                                                                                | 4.86 ms: 1.03x faster                                                                                      |
| regex_v8                   | 31.1 ms                                                                                                | 30.4 ms: 1.02x faster                                                                                      |
| deepcopy_memo              | 50.8 us                                                                                                | 49.7 us: 1.02x faster                                                                                      |
| gc_traversal               | 5.17 ms                                                                                                | 5.08 ms: 1.02x faster                                                                                      |
| mako                       | 13.2 ms                                                                                                | 13.0 ms: 1.01x faster                                                                                      |
| pickle_list                | 5.27 us                                                                                                | 5.30 us: 1.01x slower                                                                                      |
| xml_etree_iterparse        | 147 ms                                                                                                 | 148 ms: 1.01x slower                                                                                       |
| nbody                      | 114 ms                                                                                                 | 116 ms: 1.01x slower                                                                                       |
| json_dumps                 | 13.1 ms                                                                                                | 13.3 ms: 1.02x slower                                                                                      |
| asyncio_tcp_ssl            | 2.21 sec                                                                                               | 2.25 sec: 1.02x slower                                                                                     |
| richards_super             | 62.3 ms                                                                                                | 63.4 ms: 1.02x slower                                                                                      |
| pathlib                    | 22.8 ms                                                                                                | 23.2 ms: 1.02x slower                                                                                      |
| bpe_tokeniser              | 5.83 sec                                                                                               | 5.97 sec: 1.03x slower                                                                                     |
| tomli_loads                | 2.57 sec                                                                                               | 2.64 sec: 1.03x slower                                                                                     |
| chameleon                  | 8.95 ms                                                                                                | 9.18 ms: 1.03x slower                                                                                      |
| fannkuch                   | 451 ms                                                                                                 | 463 ms: 1.03x slower                                                                                       |
| logging_format             | 7.82 us                                                                                                | 8.05 us: 1.03x slower                                                                                      |
| scimark_fft                | 445 ms                                                                                                 | 459 ms: 1.03x slower                                                                                       |
| mdp                        | 3.33 sec                                                                                               | 3.44 sec: 1.03x slower                                                                                     |
| async_tree_none            | 492 ms                                                                                                 | 508 ms: 1.03x slower                                                                                       |
| async_tree_cpu_io_mixed    | 791 ms                                                                                                 | 818 ms: 1.03x slower                                                                                       |
| meteor_contest             | 113 ms                                                                                                 | 118 ms: 1.04x slower                                                                                       |
| async_tree_memoization     | 645 ms                                                                                                 | 671 ms: 1.04x slower                                                                                       |
| async_generators           | 488 ms                                                                                                 | 508 ms: 1.04x slower                                                                                       |
| bench_thread_pool          | 1.26 ms                                                                                                | 1.32 ms: 1.05x slower                                                                                      |
| spectral_norm              | 141 ms                                                                                                 | 149 ms: 1.05x slower                                                                                       |
| logging_silent             | 133 ns                                                                                                 | 141 ns: 1.06x slower                                                                                       |
| async_tree_cpu_io_mixed_tg | 763 ms                                                                                                 | 806 ms: 1.06x slower                                                                                       |
| asyncio_tcp                | 584 ms                                                                                                 | 618 ms: 1.06x slower                                                                                       |
| scimark_sparse_mat_mult    | 6.55 ms                                                                                                | 6.94 ms: 1.06x slower                                                                                      |
| dask                       | 370 ms                                                                                                 | 393 ms: 1.06x slower                                                                                       |
| generators                 | 37.1 ms                                                                                                | 39.6 ms: 1.07x slower                                                                                      |
| typing_runtime_protocols   | 193 us                                                                                                 | 207 us: 1.07x slower                                                                                       |
| pyflate                    | 557 ms                                                                                                 | 596 ms: 1.07x slower                                                                                       |
| scimark_monte_carlo        | 82.3 ms                                                                                                | 89.0 ms: 1.08x slower                                                                                      |
| raytrace                   | 297 ms                                                                                                 | 321 ms: 1.08x slower                                                                                       |
| tornado_http               | 128 ms                                                                                                 | 139 ms: 1.08x slower                                                                                       |
| html5lib                   | 66.1 ms                                                                                                | 71.7 ms: 1.09x slower                                                                                      |
| aiohttp                    | 1.18 ms                                                                                                | 1.28 ms: 1.09x slower                                                                                      |
| crypto_pyaes               | 82.0 ms                                                                                                | 89.1 ms: 1.09x slower                                                                                      |
| scimark_sor                | 159 ms                                                                                                 | 174 ms: 1.09x slower                                                                                       |
| flaskblogging              | 4.70 ms                                                                                                | 5.16 ms: 1.10x slower                                                                                      |
| unpickle_pure_python       | 251 us                                                                                                 | 278 us: 1.11x slower                                                                                       |
| pycparser                  | 1.22 sec                                                                                               | 1.35 sec: 1.11x slower                                                                                     |
| sqlglot_parse              | 1.42 ms                                                                                                | 1.58 ms: 1.11x slower                                                                                      |
| pickle_pure_python         | 359 us                                                                                                 | 398 us: 1.11x slower                                                                                       |
| sqlglot_optimize           | 62.6 ms                                                                                                | 69.8 ms: 1.11x slower                                                                                      |
| go                         | 161 ms                                                                                                 | 180 ms: 1.12x slower                                                                                       |
| sqlglot_normalize          | 129 ms                                                                                                 | 144 ms: 1.12x slower                                                                                       |
| deepcopy                   | 448 us                                                                                                 | 502 us: 1.12x slower                                                                                       |
| comprehensions             | 20.5 us                                                                                                | 23.2 us: 1.13x slower                                                                                      |
| docutils                   | 3.10 sec                                                                                               | 3.52 sec: 1.14x slower                                                                                     |
| gunicorn                   | 1.19 ms                                                                                                | 1.36 ms: 1.15x slower                                                                                      |
| deepcopy_reduce            | 4.04 us                                                                                                | 4.68 us: 1.16x slower                                                                                      |
| sqlglot_transpile          | 1.71 ms                                                                                                | 2.00 ms: 1.17x slower                                                                                      |
| django_template            | 42.3 ms                                                                                                | 49.6 ms: 1.17x slower                                                                                      |
| bench_mp_pool              | 7.03 ms                                                                                                | 8.24 ms: 1.17x slower                                                                                      |
| sympy_expand               | 457 ms                                                                                                 | 538 ms: 1.18x slower                                                                                       |
| python_startup             | 13.0 ms                                                                                                | 15.3 ms: 1.18x slower                                                                                      |
| deltablue                  | 3.88 ms                                                                                                | 4.58 ms: 1.18x slower                                                                                      |
| 2to3                       | 305 ms                                                                                                 | 360 ms: 1.18x slower                                                                                       |
| nqueens                    | 98.9 ms                                                                                                | 117 ms: 1.18x slower                                                                                       |
| pprint_safe_repr           | 933 ms                                                                                                 | 1.11 sec: 1.19x slower                                                                                     |
| pprint_pformat             | 1.93 sec                                                                                               | 2.31 sec: 1.20x slower                                                                                     |
| sympy_str                  | 265 ms                                                                                                 | 321 ms: 1.21x slower                                                                                       |
| mypy2                      | 767 ms                                                                                                 | 929 ms: 1.21x slower                                                                                       |
| dulwich_log                | 58.5 ms                                                                                                | 71.0 ms: 1.21x slower                                                                                      |
| sympy_integrate            | 20.9 ms                                                                                                | 25.5 ms: 1.22x slower                                                                                      |
| pylint                     | 337 ms                                                                                                 | 414 ms: 1.23x slower                                                                                       |
| hexiom                     | 7.08 ms                                                                                                | 8.89 ms: 1.26x slower                                                                                      |
| python_startup_no_site     | 8.60 ms                                                                                                | 10.9 ms: 1.26x slower                                                                                      |
| sympy_sum                  | 144 ms                                                                                                 | 183 ms: 1.27x slower                                                                                       |
| chaos                      | 68.3 ms                                                                                                | 87.1 ms: 1.28x slower                                                                                      |
| genshi_text                | 27.4 ms                                                                                                | 35.4 ms: 1.29x slower                                                                                      |
| scimark_lu                 | 141 ms                                                                                                 | 183 ms: 1.29x slower                                                                                       |
| regex_compile              | 128 ms                                                                                                 | 175 ms: 1.37x slower                                                                                       |
| genshi_xml                 | 60.4 ms                                                                                                | 83.4 ms: 1.38x slower                                                                                      |
| Geometric mean             | (ref)                                                                                                  | 1.08x slower                                                                                               |

Benchmark hidden because not significant (21): xml_etree_parse, xml_etree_process, coroutines, unpickle, coverage, pickle_dict, json_loads, pidigits, asyncio_websockets, xml_etree_generate, thrift, richards, unpickle_list, pickle, telco, logging_simple, json, create_gc_cycles, async_tree_none_tg, async_tree_io, async_tree_memoization_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x