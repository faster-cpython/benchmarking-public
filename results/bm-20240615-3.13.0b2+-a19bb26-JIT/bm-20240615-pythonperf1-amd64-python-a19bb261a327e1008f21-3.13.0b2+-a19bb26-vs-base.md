# Results vs. base

- fork: python
- ref: a19bb261a327e1008f21
- machine: windows-amd64
- commit hash: a19bb26
- commit date: 2024-06-15
- overall geometric mean: 1.03x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240615-3.13.0b2+-a19bb26/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json | results/bm-20240615-3.13.0b2+-a19bb26-JIT/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                                                                                 | 229 ms: 1.11x slower                                                                                                       |
| chameleon      | 4.71 ms                                                                                                                | 4.95 ms: 1.05x slower                                                                                                      |
| docutils       | 1.63 sec                                                                                                               | 1.78 sec: 1.09x slower                                                                                                     |
| html5lib       | 35.5 ms                                                                                                                | 37.8 ms: 1.07x slower                                                                                                      |
| tornado_http   | 82.1 ms                                                                                                                | 85.7 ms: 1.04x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.07x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240615-3.13.0b2+-a19bb26/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json | results/bm-20240615-3.13.0b2+-a19bb26-JIT/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 385 ms                                                                                                                 | 397 ms: 1.03x slower                                                                                                       |
| async_tree_io             | 584 ms                                                                                                                 | 603 ms: 1.03x slower                                                                                                       |
| async_tree_none_tg        | 205 ms                                                                                                                 | 214 ms: 1.05x slower                                                                                                       |
| async_tree_memoization    | 263 ms                                                                                                                 | 276 ms: 1.05x slower                                                                                                       |
| async_tree_none           | 217 ms                                                                                                                 | 228 ms: 1.05x slower                                                                                                       |
| async_tree_memoization_tg | 260 ms                                                                                                                 | 273 ms: 1.05x slower                                                                                                       |
| Geometric mean            | (ref)                                                                                                                  | 1.03x slower                                                                                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240615-3.13.0b2+-a19bb26/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json | results/bm-20240615-3.13.0b2+-a19bb26-JIT/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 69.4 ms                                                                                                                | 51.4 ms: 1.35x faster                                                                                                      |
| float          | 50.9 ms                                                                                                                | 43.5 ms: 1.17x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.16x faster                                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240615-3.13.0b2+-a19bb26/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json | results/bm-20240615-3.13.0b2+-a19bb26-JIT/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                                                                                 | 119 ms: 1.01x slower                                                                                                       |
| regex_effbot   | 1.56 ms                                                                                                                | 1.57 ms: 1.01x slower                                                                                                      |
| regex_compile  | 77.0 ms                                                                                                                | 88.9 ms: 1.15x slower                                                                                                      |
| regex_v8       | 16.2 ms                                                                                                                | 22.7 ms: 1.40x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.13x slower                                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240615-3.13.0b2+-a19bb26/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json | results/bm-20240615-3.13.0b2+-a19bb26-JIT/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.38 sec                                                                                                               | 1.21 sec: 1.14x faster                                                                                                     |
| pickle_dict          | 19.2 us                                                                                                                | 17.5 us: 1.10x faster                                                                                                      |
| pickle_list          | 3.02 us                                                                                                                | 2.86 us: 1.06x faster                                                                                                      |
| xml_etree_generate   | 53.5 ms                                                                                                                | 51.3 ms: 1.04x faster                                                                                                      |
| xml_etree_iterparse  | 62.9 ms                                                                                                                | 60.6 ms: 1.04x faster                                                                                                      |
| pickle_pure_python   | 176 us                                                                                                                 | 172 us: 1.02x faster                                                                                                       |
| unpickle_pure_python | 124 us                                                                                                                 | 125 us: 1.01x slower                                                                                                       |
| unpickle             | 8.79 us                                                                                                                | 8.98 us: 1.02x slower                                                                                                      |
| json_dumps           | 5.51 ms                                                                                                                | 5.69 ms: 1.03x slower                                                                                                      |
| unpickle_list        | 2.66 us                                                                                                                | 2.85 us: 1.07x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.02x faster                                                                                                               |

Benchmark hidden because not significant (4): xml_etree_process, json_loads, pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240615-3.13.0b2+-a19bb26/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json | results/bm-20240615-3.13.0b2+-a19bb26-JIT/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 20.2 ms                                                                                                                | 22.0 ms: 1.09x slower                                                                                                      |
| python_startup_no_site | 16.1 ms                                                                                                                | 17.8 ms: 1.10x slower                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.10x slower                                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240615-3.13.0b2+-a19bb26/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json | results/bm-20240615-3.13.0b2+-a19bb26-JIT/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.39 ms                                                                                                                | 5.18 ms: 1.23x faster                                                                                                      |
| django_template | 21.9 ms                                                                                                                | 25.4 ms: 1.16x slower                                                                                                      |
| genshi_text     | 14.8 ms                                                                                                                | 18.0 ms: 1.21x slower                                                                                                      |
| genshi_xml      | 31.1 ms                                                                                                                | 44.6 ms: 1.43x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.13x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                 | results/bm-20240615-3.13.0b2+-a19bb26/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json | results/bm-20240615-3.13.0b2+-a19bb26-JIT/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm             | 62.0 ms                                                                                                                | 45.1 ms: 1.38x faster                                                                                                      |
| nbody                     | 69.4 ms                                                                                                                | 51.4 ms: 1.35x faster                                                                                                      |
| mako                      | 6.39 ms                                                                                                                | 5.18 ms: 1.23x faster                                                                                                      |
| float                     | 50.9 ms                                                                                                                | 43.5 ms: 1.17x faster                                                                                                      |
| scimark_fft               | 175 ms                                                                                                                 | 152 ms: 1.16x faster                                                                                                       |
| scimark_sparse_mat_mult   | 2.46 ms                                                                                                                | 2.14 ms: 1.15x faster                                                                                                      |
| tomli_loads               | 1.38 sec                                                                                                               | 1.21 sec: 1.14x faster                                                                                                     |
| deepcopy_memo             | 22.6 us                                                                                                                | 20.1 us: 1.12x faster                                                                                                      |
| pickle_dict               | 19.2 us                                                                                                                | 17.5 us: 1.10x faster                                                                                                      |
| crypto_pyaes              | 44.8 ms                                                                                                                | 41.0 ms: 1.09x faster                                                                                                      |
| scimark_monte_carlo       | 41.6 ms                                                                                                                | 38.2 ms: 1.09x faster                                                                                                      |
| pyflate                   | 281 ms                                                                                                                 | 259 ms: 1.09x faster                                                                                                       |
| json                      | 3.12 ms                                                                                                                | 2.90 ms: 1.07x faster                                                                                                      |
| fannkuch                  | 241 ms                                                                                                                 | 226 ms: 1.07x faster                                                                                                       |
| asyncio_tcp_ssl           | 1.54 sec                                                                                                               | 1.45 sec: 1.06x faster                                                                                                     |
| pickle_list               | 3.02 us                                                                                                                | 2.86 us: 1.06x faster                                                                                                      |
| pprint_pformat            | 980 ms                                                                                                                 | 929 ms: 1.05x faster                                                                                                       |
| pprint_safe_repr          | 476 ms                                                                                                                 | 452 ms: 1.05x faster                                                                                                       |
| telco                     | 4.76 ms                                                                                                                | 4.56 ms: 1.04x faster                                                                                                      |
| xml_etree_generate        | 53.5 ms                                                                                                                | 51.3 ms: 1.04x faster                                                                                                      |
| xml_etree_iterparse       | 62.9 ms                                                                                                                | 60.6 ms: 1.04x faster                                                                                                      |
| sqlite_synth              | 1.62 us                                                                                                                | 1.58 us: 1.03x faster                                                                                                      |
| mdp                       | 1.39 sec                                                                                                               | 1.36 sec: 1.03x faster                                                                                                     |
| pickle_pure_python        | 176 us                                                                                                                 | 172 us: 1.02x faster                                                                                                       |
| coverage                  | 45.4 ms                                                                                                                | 44.5 ms: 1.02x faster                                                                                                      |
| comprehensions            | 10.2 us                                                                                                                | 10.2 us: 1.00x faster                                                                                                      |
| regex_dna                 | 118 ms                                                                                                                 | 119 ms: 1.01x slower                                                                                                       |
| regex_effbot              | 1.56 ms                                                                                                                | 1.57 ms: 1.01x slower                                                                                                      |
| gc_traversal              | 1.55 ms                                                                                                                | 1.57 ms: 1.01x slower                                                                                                      |
| unpickle_pure_python      | 124 us                                                                                                                 | 125 us: 1.01x slower                                                                                                       |
| pathlib                   | 75.1 ms                                                                                                                | 76.0 ms: 1.01x slower                                                                                                      |
| deepcopy_reduce           | 2.05 us                                                                                                                | 2.08 us: 1.02x slower                                                                                                      |
| coroutines                | 13.3 ms                                                                                                                | 13.5 ms: 1.02x slower                                                                                                      |
| unpickle                  | 8.79 us                                                                                                                | 8.98 us: 1.02x slower                                                                                                      |
| chaos                     | 38.2 ms                                                                                                                | 39.2 ms: 1.03x slower                                                                                                      |
| async_tree_cpu_io_mixed   | 385 ms                                                                                                                 | 397 ms: 1.03x slower                                                                                                       |
| async_tree_io             | 584 ms                                                                                                                 | 603 ms: 1.03x slower                                                                                                       |
| json_dumps                | 5.51 ms                                                                                                                | 5.69 ms: 1.03x slower                                                                                                      |
| meteor_contest            | 71.6 ms                                                                                                                | 74.1 ms: 1.04x slower                                                                                                      |
| aiohttp                   | 899 us                                                                                                                 | 932 us: 1.04x slower                                                                                                       |
| bench_thread_pool         | 763 us                                                                                                                 | 792 us: 1.04x slower                                                                                                       |
| tornado_http              | 82.1 ms                                                                                                                | 85.7 ms: 1.04x slower                                                                                                      |
| async_tree_none_tg        | 205 ms                                                                                                                 | 214 ms: 1.05x slower                                                                                                       |
| async_tree_memoization    | 263 ms                                                                                                                 | 276 ms: 1.05x slower                                                                                                       |
| async_tree_none           | 217 ms                                                                                                                 | 228 ms: 1.05x slower                                                                                                       |
| dulwich_log               | 38.9 ms                                                                                                                | 40.7 ms: 1.05x slower                                                                                                      |
| async_tree_memoization_tg | 260 ms                                                                                                                 | 273 ms: 1.05x slower                                                                                                       |
| logging_silent            | 53.0 ns                                                                                                                | 55.6 ns: 1.05x slower                                                                                                      |
| chameleon                 | 4.71 ms                                                                                                                | 4.95 ms: 1.05x slower                                                                                                      |
| typing_runtime_protocols  | 104 us                                                                                                                 | 110 us: 1.06x slower                                                                                                       |
| sqlglot_parse             | 765 us                                                                                                                 | 809 us: 1.06x slower                                                                                                       |
| nqueens                   | 57.0 ms                                                                                                                | 60.5 ms: 1.06x slower                                                                                                      |
| deepcopy                  | 223 us                                                                                                                 | 237 us: 1.06x slower                                                                                                       |
| sqlglot_transpile         | 975 us                                                                                                                 | 1.04 ms: 1.07x slower                                                                                                      |
| html5lib                  | 35.5 ms                                                                                                                | 37.8 ms: 1.07x slower                                                                                                      |
| bench_mp_pool             | 64.5 ms                                                                                                                | 68.9 ms: 1.07x slower                                                                                                      |
| unpickle_list             | 2.66 us                                                                                                                | 2.85 us: 1.07x slower                                                                                                      |
| richards                  | 26.6 ms                                                                                                                | 29.1 ms: 1.09x slower                                                                                                      |
| docutils                  | 1.63 sec                                                                                                               | 1.78 sec: 1.09x slower                                                                                                     |
| python_startup            | 20.2 ms                                                                                                                | 22.0 ms: 1.09x slower                                                                                                      |
| scimark_sor               | 75.5 ms                                                                                                                | 82.7 ms: 1.10x slower                                                                                                      |
| richards_super            | 30.1 ms                                                                                                                | 33.0 ms: 1.10x slower                                                                                                      |
| raytrace                  | 159 ms                                                                                                                 | 175 ms: 1.10x slower                                                                                                       |
| python_startup_no_site    | 16.1 ms                                                                                                                | 17.8 ms: 1.10x slower                                                                                                      |
| sympy_sum                 | 84.9 ms                                                                                                                | 93.6 ms: 1.10x slower                                                                                                      |
| 2to3                      | 207 ms                                                                                                                 | 229 ms: 1.11x slower                                                                                                       |
| sqlglot_optimize          | 33.3 ms                                                                                                                | 36.9 ms: 1.11x slower                                                                                                      |
| sympy_str                 | 162 ms                                                                                                                 | 180 ms: 1.11x slower                                                                                                       |
| async_generators          | 223 ms                                                                                                                 | 250 ms: 1.12x slower                                                                                                       |
| generators                | 20.1 ms                                                                                                                | 22.5 ms: 1.12x slower                                                                                                      |
| thrift                    | 7.96 ms                                                                                                                | 8.96 ms: 1.13x slower                                                                                                      |
| go                        | 82.5 ms                                                                                                                | 93.2 ms: 1.13x slower                                                                                                      |
| sympy_integrate           | 12.4 ms                                                                                                                | 14.1 ms: 1.14x slower                                                                                                      |
| sympy_expand              | 275 ms                                                                                                                 | 316 ms: 1.15x slower                                                                                                       |
| pylint                    | 205 ms                                                                                                                 | 236 ms: 1.15x slower                                                                                                       |
| regex_compile             | 77.0 ms                                                                                                                | 88.9 ms: 1.15x slower                                                                                                      |
| django_template           | 21.9 ms                                                                                                                | 25.4 ms: 1.16x slower                                                                                                      |
| genshi_text               | 14.8 ms                                                                                                                | 18.0 ms: 1.21x slower                                                                                                      |
| deltablue                 | 1.89 ms                                                                                                                | 2.36 ms: 1.25x slower                                                                                                      |
| hexiom                    | 3.70 ms                                                                                                                | 4.68 ms: 1.27x slower                                                                                                      |
| scimark_lu                | 54.0 ms                                                                                                                | 69.6 ms: 1.29x slower                                                                                                      |
| regex_v8                  | 16.2 ms                                                                                                                | 22.7 ms: 1.40x slower                                                                                                      |
| genshi_xml                | 31.1 ms                                                                                                                | 44.6 ms: 1.43x slower                                                                                                      |
| Geometric mean            | (ref)                                                                                                                  | 1.03x slower                                                                                                               |

Benchmark hidden because not significant (13): asyncio_tcp, xml_etree_process, logging_simple, json_loads, logging_format, flaskblogging, pickle, pidigits, create_gc_cycles, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_io_tg, pycparser
Ignored benchmarks (2) of results/bm-20240615-3.13.0b2+-a19bb26/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json: mypy2, sqlglot_normalize

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown