# Results vs. base

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-amd64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.015x faster
- HPT reliability: 76.86%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.65 sec                                                                                                               | 1.74 sec: 1.05x slower                                                                                                     |
| sphinx         | 643 ms                                                                                                                 | 656 ms: 1.02x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg          | 428 ms                                                                                                                 | 403 ms: 1.06x faster                                                                                                       |
| coroutines                | 13.3 ms                                                                                                                | 12.8 ms: 1.04x faster                                                                                                      |
| async_tree_none_tg        | 179 ms                                                                                                                 | 174 ms: 1.03x faster                                                                                                       |
| async_tree_none           | 190 ms                                                                                                                 | 186 ms: 1.02x faster                                                                                                       |
| async_tree_memoization_tg | 218 ms                                                                                                                 | 215 ms: 1.02x faster                                                                                                       |
| async_tree_memoization    | 224 ms                                                                                                                 | 222 ms: 1.01x faster                                                                                                       |
| async_tree_cpu_io_mixed   | 339 ms                                                                                                                 | 342 ms: 1.01x slower                                                                                                       |
| asyncio_websockets        | 312 ms                                                                                                                 | 317 ms: 1.02x slower                                                                                                       |
| async_generators          | 222 ms                                                                                                                 | 240 ms: 1.08x slower                                                                                                       |
| Geometric mean            | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, asyncio_tcp, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 69.1 ms                                                                                                                | 57.1 ms: 1.21x faster                                                                                                      |
| pidigits       | 151 ms                                                                                                                 | 152 ms: 1.01x slower                                                                                                       |
| float          | 45.1 ms                                                                                                                | 46.1 ms: 1.02x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.06x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 84.1 ms                                                                                                                | 82.2 ms: 1.02x faster                                                                                                      |
| regex_v8       | 14.3 ms                                                                                                                | 15.0 ms: 1.05x slower                                                                                                      |
| regex_dna      | 112 ms                                                                                                                 | 117 ms: 1.05x slower                                                                                                       |
| regex_effbot   | 1.40 ms                                                                                                                | 1.51 ms: 1.08x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.04x slower                                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 142 us                                                                                                                 | 113 us: 1.25x faster                                                                                                       |
| tomli_loads          | 1.35 sec                                                                                                               | 1.19 sec: 1.14x faster                                                                                                     |
| xml_etree_generate   | 56.5 ms                                                                                                                | 50.8 ms: 1.11x faster                                                                                                      |
| unpickle_list        | 2.84 us                                                                                                                | 2.63 us: 1.08x faster                                                                                                      |
| xml_etree_process    | 39.6 ms                                                                                                                | 36.7 ms: 1.08x faster                                                                                                      |
| xml_etree_iterparse  | 62.9 ms                                                                                                                | 61.1 ms: 1.03x faster                                                                                                      |
| pickle               | 7.87 us                                                                                                                | 7.81 us: 1.01x faster                                                                                                      |
| unpickle             | 8.40 us                                                                                                                | 8.51 us: 1.01x slower                                                                                                      |
| pickle_list          | 2.96 us                                                                                                                | 3.00 us: 1.01x slower                                                                                                      |
| json_loads           | 15.2 us                                                                                                                | 15.5 us: 1.02x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.04x faster                                                                                                               |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_dict, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.69 ms                                                                                                                | 5.24 ms: 1.28x faster                                                                                                      |
| genshi_text    | 15.8 ms                                                                                                                | 16.0 ms: 1.01x slower                                                                                                      |
| genshi_xml     | 34.7 ms                                                                                                                | 35.4 ms: 1.02x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.05x faster                                                                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako                      | 6.69 ms                                                                                                                | 5.24 ms: 1.28x faster                                                                                                      |
| scimark_sparse_mat_mult   | 2.62 ms                                                                                                                | 2.09 ms: 1.25x faster                                                                                                      |
| unpickle_pure_python      | 142 us                                                                                                                 | 113 us: 1.25x faster                                                                                                       |
| scimark_fft               | 183 ms                                                                                                                 | 148 ms: 1.24x faster                                                                                                       |
| nbody                     | 69.1 ms                                                                                                                | 57.1 ms: 1.21x faster                                                                                                      |
| tomli_loads               | 1.35 sec                                                                                                               | 1.19 sec: 1.14x faster                                                                                                     |
| bpe_tokeniser             | 2.87 sec                                                                                                               | 2.56 sec: 1.12x faster                                                                                                     |
| xml_etree_generate        | 56.5 ms                                                                                                                | 50.8 ms: 1.11x faster                                                                                                      |
| pyflate                   | 303 ms                                                                                                                 | 273 ms: 1.11x faster                                                                                                       |
| fannkuch                  | 262 ms                                                                                                                 | 239 ms: 1.10x faster                                                                                                       |
| sqlite_synth              | 1.67 us                                                                                                                | 1.54 us: 1.09x faster                                                                                                      |
| pprint_pformat            | 1.06 sec                                                                                                               | 975 ms: 1.09x faster                                                                                                       |
| unpickle_list             | 2.84 us                                                                                                                | 2.63 us: 1.08x faster                                                                                                      |
| xml_etree_process         | 39.6 ms                                                                                                                | 36.7 ms: 1.08x faster                                                                                                      |
| async_tree_io_tg          | 428 ms                                                                                                                 | 403 ms: 1.06x faster                                                                                                       |
| telco                     | 4.79 ms                                                                                                                | 4.55 ms: 1.05x faster                                                                                                      |
| k_core                    | 1.72 sec                                                                                                               | 1.64 sec: 1.05x faster                                                                                                     |
| sqlglot_parse             | 875 us                                                                                                                 | 842 us: 1.04x faster                                                                                                       |
| coroutines                | 13.3 ms                                                                                                                | 12.8 ms: 1.04x faster                                                                                                      |
| async_tree_none_tg        | 179 ms                                                                                                                 | 174 ms: 1.03x faster                                                                                                       |
| comprehensions            | 11.6 us                                                                                                                | 11.2 us: 1.03x faster                                                                                                      |
| xml_etree_iterparse       | 62.9 ms                                                                                                                | 61.1 ms: 1.03x faster                                                                                                      |
| subparsers                | 16.4 ms                                                                                                                | 16.0 ms: 1.03x faster                                                                                                      |
| crypto_pyaes              | 46.9 ms                                                                                                                | 45.8 ms: 1.02x faster                                                                                                      |
| regex_compile             | 84.1 ms                                                                                                                | 82.2 ms: 1.02x faster                                                                                                      |
| async_tree_none           | 190 ms                                                                                                                 | 186 ms: 1.02x faster                                                                                                       |
| pycparser                 | 725 ms                                                                                                                 | 713 ms: 1.02x faster                                                                                                       |
| raytrace                  | 198 ms                                                                                                                 | 195 ms: 1.02x faster                                                                                                       |
| async_tree_memoization_tg | 218 ms                                                                                                                 | 215 ms: 1.02x faster                                                                                                       |
| scimark_sor               | 85.4 ms                                                                                                                | 84.2 ms: 1.01x faster                                                                                                      |
| connected_components      | 318 ms                                                                                                                 | 314 ms: 1.01x faster                                                                                                       |
| async_tree_memoization    | 224 ms                                                                                                                 | 222 ms: 1.01x faster                                                                                                       |
| sqlglot_transpile         | 1.07 ms                                                                                                                | 1.06 ms: 1.01x faster                                                                                                      |
| nqueens                   | 62.6 ms                                                                                                                | 62.0 ms: 1.01x faster                                                                                                      |
| bench_mp_pool             | 90.8 ms                                                                                                                | 89.9 ms: 1.01x faster                                                                                                      |
| pickle                    | 7.87 us                                                                                                                | 7.81 us: 1.01x faster                                                                                                      |
| shortest_path             | 349 ms                                                                                                                 | 347 ms: 1.01x faster                                                                                                       |
| dulwich_log               | 42.2 ms                                                                                                                | 42.5 ms: 1.01x slower                                                                                                      |
| async_tree_cpu_io_mixed   | 339 ms                                                                                                                 | 342 ms: 1.01x slower                                                                                                       |
| logging_format            | 6.77 us                                                                                                                | 6.83 us: 1.01x slower                                                                                                      |
| pidigits                  | 151 ms                                                                                                                 | 152 ms: 1.01x slower                                                                                                       |
| many_optionals            | 437 us                                                                                                                 | 441 us: 1.01x slower                                                                                                       |
| sympy_sum                 | 89.4 ms                                                                                                                | 90.5 ms: 1.01x slower                                                                                                      |
| unpickle                  | 8.40 us                                                                                                                | 8.51 us: 1.01x slower                                                                                                      |
| genshi_text               | 15.8 ms                                                                                                                | 16.0 ms: 1.01x slower                                                                                                      |
| pickle_list               | 2.96 us                                                                                                                | 3.00 us: 1.01x slower                                                                                                      |
| logging_simple            | 6.32 us                                                                                                                | 6.41 us: 1.01x slower                                                                                                      |
| create_gc_cycles          | 1.22 ms                                                                                                                | 1.24 ms: 1.02x slower                                                                                                      |
| deepcopy                  | 183 us                                                                                                                 | 186 us: 1.02x slower                                                                                                       |
| asyncio_websockets        | 312 ms                                                                                                                 | 317 ms: 1.02x slower                                                                                                       |
| generators                | 19.8 ms                                                                                                                | 20.2 ms: 1.02x slower                                                                                                      |
| json_loads                | 15.2 us                                                                                                                | 15.5 us: 1.02x slower                                                                                                      |
| typing_runtime_protocols  | 106 us                                                                                                                 | 108 us: 1.02x slower                                                                                                       |
| sphinx                    | 643 ms                                                                                                                 | 656 ms: 1.02x slower                                                                                                       |
| sympy_str                 | 174 ms                                                                                                                 | 177 ms: 1.02x slower                                                                                                       |
| richards_super            | 32.9 ms                                                                                                                | 33.6 ms: 1.02x slower                                                                                                      |
| genshi_xml                | 34.7 ms                                                                                                                | 35.4 ms: 1.02x slower                                                                                                      |
| float                     | 45.1 ms                                                                                                                | 46.1 ms: 1.02x slower                                                                                                      |
| coverage                  | 48.5 ms                                                                                                                | 49.6 ms: 1.02x slower                                                                                                      |
| deepcopy_reduce           | 1.90 us                                                                                                                | 1.95 us: 1.02x slower                                                                                                      |
| scimark_monte_carlo       | 44.3 ms                                                                                                                | 45.4 ms: 1.02x slower                                                                                                      |
| go                        | 85.4 ms                                                                                                                | 87.6 ms: 1.03x slower                                                                                                      |
| sympy_expand              | 299 ms                                                                                                                 | 307 ms: 1.03x slower                                                                                                       |
| sympy_integrate           | 13.1 ms                                                                                                                | 13.5 ms: 1.03x slower                                                                                                      |
| json                      | 3.02 ms                                                                                                                | 3.12 ms: 1.03x slower                                                                                                      |
| richards                  | 28.7 ms                                                                                                                | 29.7 ms: 1.03x slower                                                                                                      |
| logging_silent            | 57.2 ns                                                                                                                | 59.5 ns: 1.04x slower                                                                                                      |
| hexiom                    | 4.23 ms                                                                                                                | 4.42 ms: 1.05x slower                                                                                                      |
| regex_v8                  | 14.3 ms                                                                                                                | 15.0 ms: 1.05x slower                                                                                                      |
| regex_dna                 | 112 ms                                                                                                                 | 117 ms: 1.05x slower                                                                                                       |
| docutils                  | 1.65 sec                                                                                                               | 1.74 sec: 1.05x slower                                                                                                     |
| sqlglot_optimize          | 35.2 ms                                                                                                                | 37.6 ms: 1.07x slower                                                                                                      |
| sqlglot_normalize         | 189 ms                                                                                                                 | 203 ms: 1.07x slower                                                                                                       |
| regex_effbot              | 1.40 ms                                                                                                                | 1.51 ms: 1.08x slower                                                                                                      |
| async_generators          | 222 ms                                                                                                                 | 240 ms: 1.08x slower                                                                                                       |
| deltablue                 | 2.15 ms                                                                                                                | 2.34 ms: 1.09x slower                                                                                                      |
| mdp                       | 1.46 sec                                                                                                               | 1.60 sec: 1.09x slower                                                                                                     |
| unpack_sequence           | 36.9 ns                                                                                                                | 43.6 ns: 1.18x slower                                                                                                      |
| Geometric mean            | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (24): pprint_safe_repr, 2to3, pathlib, spectral_norm, asyncio_tcp_ssl, chaos, bench_thread_pool, django_template, xml_etree_parse, meteor_contest, async_tree_cpu_io_mixed_tg, deepcopy_memo, thrift, pickle_dict, pickle_pure_python, json_dumps, asyncio_tcp, python_startup_no_site, async_tree_io, gc_traversal, scimark_lu, python_startup, html5lib, pylint

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 76.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown