# Results vs. base

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-amd64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.012x faster
- HPT reliability: 91.28%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.64 sec                                                                                                               | 1.73 sec: 1.05x slower                                                                                                     |
| html5lib       | 37.4 ms                                                                                                                | 38.3 ms: 1.02x slower                                                                                                      |
| sphinx         | 638 ms                                                                                                                 | 669 ms: 1.05x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.03x slower                                                                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 172 ms                                                                                                                 | 167 ms: 1.03x faster                                                                                                       |
| coroutines                 | 13.2 ms                                                                                                                | 12.8 ms: 1.03x faster                                                                                                      |
| asyncio_websockets         | 312 ms                                                                                                                 | 306 ms: 1.02x faster                                                                                                       |
| async_tree_none            | 181 ms                                                                                                                 | 178 ms: 1.02x faster                                                                                                       |
| async_tree_memoization     | 217 ms                                                                                                                 | 213 ms: 1.02x faster                                                                                                       |
| async_tree_io_tg           | 400 ms                                                                                                                 | 394 ms: 1.02x faster                                                                                                       |
| async_tree_cpu_io_mixed_tg | 340 ms                                                                                                                 | 336 ms: 1.01x faster                                                                                                       |
| async_generators           | 216 ms                                                                                                                 | 233 ms: 1.08x slower                                                                                                       |
| asyncio_tcp_ssl            | 1.35 sec                                                                                                               | 1.45 sec: 1.08x slower                                                                                                     |
| asyncio_tcp                | 452 ms                                                                                                                 | 543 ms: 1.20x slower                                                                                                       |
| Geometric mean             | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 64.2 ms                                                                                                                | 50.4 ms: 1.27x faster                                                                                                      |
| float          | 45.0 ms                                                                                                                | 37.0 ms: 1.21x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.16x faster                                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 1.48 ms                                                                                                                | 1.42 ms: 1.05x faster                                                                                                      |
| regex_v8       | 15.3 ms                                                                                                                | 14.8 ms: 1.04x faster                                                                                                      |
| regex_dna      | 117 ms                                                                                                                 | 115 ms: 1.02x faster                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 140 us                                                                                                                 | 110 us: 1.27x faster                                                                                                       |
| tomli_loads          | 1.31 sec                                                                                                               | 1.13 sec: 1.16x faster                                                                                                     |
| xml_etree_generate   | 54.8 ms                                                                                                                | 50.3 ms: 1.09x faster                                                                                                      |
| xml_etree_process    | 38.6 ms                                                                                                                | 35.8 ms: 1.08x faster                                                                                                      |
| json_dumps           | 6.64 ms                                                                                                                | 6.24 ms: 1.06x faster                                                                                                      |
| pickle_pure_python   | 210 us                                                                                                                 | 198 us: 1.06x faster                                                                                                       |
| xml_etree_iterparse  | 62.8 ms                                                                                                                | 59.6 ms: 1.05x faster                                                                                                      |
| unpickle_list        | 2.77 us                                                                                                                | 2.67 us: 1.04x faster                                                                                                      |
| xml_etree_parse      | 89.4 ms                                                                                                                | 88.1 ms: 1.02x faster                                                                                                      |
| json_loads           | 15.4 us                                                                                                                | 15.5 us: 1.01x slower                                                                                                      |
| pickle               | 8.01 us                                                                                                                | 8.11 us: 1.01x slower                                                                                                      |
| pickle_dict          | 18.1 us                                                                                                                | 18.4 us: 1.02x slower                                                                                                      |
| unpickle             | 8.61 us                                                                                                                | 8.77 us: 1.02x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.05x faster                                                                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                                                                                | 19.7 ms: 1.03x slower                                                                                                      |
| python_startup         | 24.9 ms                                                                                                                | 26.1 ms: 1.04x slower                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.04x slower                                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.69 ms                                                                                                                | 5.26 ms: 1.27x faster                                                                                                      |
| django_template | 23.5 ms                                                                                                                | 26.1 ms: 1.11x slower                                                                                                      |
| genshi_text     | 14.6 ms                                                                                                                | 17.1 ms: 1.17x slower                                                                                                      |
| genshi_xml      | 31.6 ms                                                                                                                | 43.3 ms: 1.37x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.09x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| scimark_sor                | 82.2 ms                                                                                                                | 57.5 ms: 1.43x faster                                                                                                      |
| nbody                      | 64.2 ms                                                                                                                | 50.4 ms: 1.27x faster                                                                                                      |
| mako                       | 6.69 ms                                                                                                                | 5.26 ms: 1.27x faster                                                                                                      |
| unpickle_pure_python       | 140 us                                                                                                                 | 110 us: 1.27x faster                                                                                                       |
| spectral_norm              | 57.8 ms                                                                                                                | 46.3 ms: 1.25x faster                                                                                                      |
| scimark_fft                | 182 ms                                                                                                                 | 146 ms: 1.24x faster                                                                                                       |
| scimark_monte_carlo        | 44.0 ms                                                                                                                | 35.9 ms: 1.22x faster                                                                                                      |
| float                      | 45.0 ms                                                                                                                | 37.0 ms: 1.21x faster                                                                                                      |
| scimark_sparse_mat_mult    | 2.61 ms                                                                                                                | 2.15 ms: 1.21x faster                                                                                                      |
| tomli_loads                | 1.31 sec                                                                                                               | 1.13 sec: 1.16x faster                                                                                                     |
| deepcopy_memo              | 18.9 us                                                                                                                | 16.5 us: 1.14x faster                                                                                                      |
| logging_silent             | 60.8 ns                                                                                                                | 54.0 ns: 1.13x faster                                                                                                      |
| bpe_tokeniser              | 2.85 sec                                                                                                               | 2.60 sec: 1.09x faster                                                                                                     |
| xml_etree_generate         | 54.8 ms                                                                                                                | 50.3 ms: 1.09x faster                                                                                                      |
| fannkuch                   | 259 ms                                                                                                                 | 237 ms: 1.09x faster                                                                                                       |
| pyflate                    | 290 ms                                                                                                                 | 267 ms: 1.09x faster                                                                                                       |
| xml_etree_process          | 38.6 ms                                                                                                                | 35.8 ms: 1.08x faster                                                                                                      |
| telco                      | 4.66 ms                                                                                                                | 4.33 ms: 1.08x faster                                                                                                      |
| json_dumps                 | 6.64 ms                                                                                                                | 6.24 ms: 1.06x faster                                                                                                      |
| pickle_pure_python         | 210 us                                                                                                                 | 198 us: 1.06x faster                                                                                                       |
| k_core                     | 1.72 sec                                                                                                               | 1.62 sec: 1.06x faster                                                                                                     |
| xml_etree_iterparse        | 62.8 ms                                                                                                                | 59.6 ms: 1.05x faster                                                                                                      |
| regex_effbot               | 1.48 ms                                                                                                                | 1.42 ms: 1.05x faster                                                                                                      |
| regex_v8                   | 15.3 ms                                                                                                                | 14.8 ms: 1.04x faster                                                                                                      |
| scimark_lu                 | 59.3 ms                                                                                                                | 57.3 ms: 1.04x faster                                                                                                      |
| unpickle_list              | 2.77 us                                                                                                                | 2.67 us: 1.04x faster                                                                                                      |
| async_tree_none_tg         | 172 ms                                                                                                                 | 167 ms: 1.03x faster                                                                                                       |
| crypto_pyaes               | 46.8 ms                                                                                                                | 45.4 ms: 1.03x faster                                                                                                      |
| coroutines                 | 13.2 ms                                                                                                                | 12.8 ms: 1.03x faster                                                                                                      |
| pprint_pformat             | 1.04 sec                                                                                                               | 1.01 sec: 1.03x faster                                                                                                     |
| asyncio_websockets         | 312 ms                                                                                                                 | 306 ms: 1.02x faster                                                                                                       |
| coverage                   | 47.1 ms                                                                                                                | 46.1 ms: 1.02x faster                                                                                                      |
| shortest_path              | 352 ms                                                                                                                 | 346 ms: 1.02x faster                                                                                                       |
| async_tree_none            | 181 ms                                                                                                                 | 178 ms: 1.02x faster                                                                                                       |
| async_tree_memoization     | 217 ms                                                                                                                 | 213 ms: 1.02x faster                                                                                                       |
| connected_components       | 320 ms                                                                                                                 | 315 ms: 1.02x faster                                                                                                       |
| xml_etree_parse            | 89.4 ms                                                                                                                | 88.1 ms: 1.02x faster                                                                                                      |
| regex_dna                  | 117 ms                                                                                                                 | 115 ms: 1.02x faster                                                                                                       |
| async_tree_io_tg           | 400 ms                                                                                                                 | 394 ms: 1.02x faster                                                                                                       |
| async_tree_cpu_io_mixed_tg | 340 ms                                                                                                                 | 336 ms: 1.01x faster                                                                                                       |
| sqlglot_parse              | 819 us                                                                                                                 | 809 us: 1.01x faster                                                                                                       |
| sqlite_synth               | 1.57 us                                                                                                                | 1.56 us: 1.01x faster                                                                                                      |
| subparsers                 | 15.7 ms                                                                                                                | 15.6 ms: 1.01x faster                                                                                                      |
| json                       | 3.11 ms                                                                                                                | 3.08 ms: 1.01x faster                                                                                                      |
| bench_mp_pool              | 89.2 ms                                                                                                                | 89.6 ms: 1.00x slower                                                                                                      |
| json_loads                 | 15.4 us                                                                                                                | 15.5 us: 1.01x slower                                                                                                      |
| pickle                     | 8.01 us                                                                                                                | 8.11 us: 1.01x slower                                                                                                      |
| sqlglot_transpile          | 1.02 ms                                                                                                                | 1.03 ms: 1.01x slower                                                                                                      |
| pickle_dict                | 18.1 us                                                                                                                | 18.4 us: 1.02x slower                                                                                                      |
| unpickle                   | 8.61 us                                                                                                                | 8.77 us: 1.02x slower                                                                                                      |
| html5lib                   | 37.4 ms                                                                                                                | 38.3 ms: 1.02x slower                                                                                                      |
| sympy_expand               | 293 ms                                                                                                                 | 300 ms: 1.02x slower                                                                                                       |
| typing_runtime_protocols   | 103 us                                                                                                                 | 105 us: 1.02x slower                                                                                                       |
| deltablue                  | 2.08 ms                                                                                                                | 2.13 ms: 1.03x slower                                                                                                      |
| meteor_contest             | 74.2 ms                                                                                                                | 76.2 ms: 1.03x slower                                                                                                      |
| comprehensions             | 11.0 us                                                                                                                | 11.3 us: 1.03x slower                                                                                                      |
| dulwich_log                | 41.4 ms                                                                                                                | 42.6 ms: 1.03x slower                                                                                                      |
| deepcopy_reduce            | 1.81 us                                                                                                                | 1.87 us: 1.03x slower                                                                                                      |
| chaos                      | 39.5 ms                                                                                                                | 40.7 ms: 1.03x slower                                                                                                      |
| sympy_str                  | 170 ms                                                                                                                 | 176 ms: 1.03x slower                                                                                                       |
| sympy_integrate            | 12.9 ms                                                                                                                | 13.3 ms: 1.03x slower                                                                                                      |
| python_startup_no_site     | 19.1 ms                                                                                                                | 19.7 ms: 1.03x slower                                                                                                      |
| pprint_safe_repr           | 513 ms                                                                                                                 | 532 ms: 1.04x slower                                                                                                       |
| nqueens                    | 59.4 ms                                                                                                                | 61.7 ms: 1.04x slower                                                                                                      |
| sympy_sum                  | 87.0 ms                                                                                                                | 90.3 ms: 1.04x slower                                                                                                      |
| python_startup             | 24.9 ms                                                                                                                | 26.1 ms: 1.04x slower                                                                                                      |
| sphinx                     | 638 ms                                                                                                                 | 669 ms: 1.05x slower                                                                                                       |
| docutils                   | 1.64 sec                                                                                                               | 1.73 sec: 1.05x slower                                                                                                     |
| many_optionals             | 421 us                                                                                                                 | 447 us: 1.06x slower                                                                                                       |
| deepcopy                   | 174 us                                                                                                                 | 185 us: 1.06x slower                                                                                                       |
| sqlglot_normalize          | 183 ms                                                                                                                 | 196 ms: 1.07x slower                                                                                                       |
| pylint                     | 191 ms                                                                                                                 | 205 ms: 1.07x slower                                                                                                       |
| async_generators           | 216 ms                                                                                                                 | 233 ms: 1.08x slower                                                                                                       |
| sqlglot_optimize           | 33.8 ms                                                                                                                | 36.4 ms: 1.08x slower                                                                                                      |
| asyncio_tcp_ssl            | 1.35 sec                                                                                                               | 1.45 sec: 1.08x slower                                                                                                     |
| go                         | 80.7 ms                                                                                                                | 87.0 ms: 1.08x slower                                                                                                      |
| django_template            | 23.5 ms                                                                                                                | 26.1 ms: 1.11x slower                                                                                                      |
| richards_super             | 31.8 ms                                                                                                                | 35.8 ms: 1.12x slower                                                                                                      |
| mdp                        | 1.46 sec                                                                                                               | 1.65 sec: 1.13x slower                                                                                                     |
| raytrace                   | 182 ms                                                                                                                 | 206 ms: 1.13x slower                                                                                                       |
| richards                   | 28.1 ms                                                                                                                | 32.0 ms: 1.14x slower                                                                                                      |
| genshi_text                | 14.6 ms                                                                                                                | 17.1 ms: 1.17x slower                                                                                                      |
| hexiom                     | 4.08 ms                                                                                                                | 4.89 ms: 1.20x slower                                                                                                      |
| asyncio_tcp                | 452 ms                                                                                                                 | 543 ms: 1.20x slower                                                                                                       |
| generators                 | 18.0 ms                                                                                                                | 24.0 ms: 1.34x slower                                                                                                      |
| genshi_xml                 | 31.6 ms                                                                                                                | 43.3 ms: 1.37x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (16): pycparser, regex_compile, 2to3, unpack_sequence, logging_format, pidigits, logging_simple, async_tree_cpu_io_mixed, pickle_list, pathlib, thrift, gc_traversal, create_gc_cycles, async_tree_io, bench_thread_pool, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 91.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown