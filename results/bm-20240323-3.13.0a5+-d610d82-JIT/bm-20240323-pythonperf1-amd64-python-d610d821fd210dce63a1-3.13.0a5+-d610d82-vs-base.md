# Results vs. base

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-amd64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.01x slower
- HPT reliability: 98.49%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 210 ms                                                                                                                 | 220 ms: 1.05x slower                                                                                                       |
| chameleon      | 4.74 ms                                                                                                                | 4.58 ms: 1.03x faster                                                                                                      |
| docutils       | 1.62 sec                                                                                                               | 1.68 sec: 1.04x slower                                                                                                     |
| html5lib       | 36.3 ms                                                                                                                | 35.8 ms: 1.01x faster                                                                                                      |
| tornado_http   | 83.2 ms                                                                                                                | 85.1 ms: 1.02x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|-------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 381 ms                                                                                                                 | 386 ms: 1.01x slower                                                                                                       |
| Geometric mean          | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 68.6 ms                                                                                                                | 57.0 ms: 1.20x faster                                                                                                      |
| float          | 52.7 ms                                                                                                                | 46.2 ms: 1.14x faster                                                                                                      |
| pidigits       | 147 ms                                                                                                                 | 150 ms: 1.02x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.10x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 1.57 ms                                                                                                                | 1.60 ms: 1.02x slower                                                                                                      |
| regex_dna      | 116 ms                                                                                                                 | 121 ms: 1.04x slower                                                                                                       |
| regex_v8       | 14.3 ms                                                                                                                | 15.3 ms: 1.07x slower                                                                                                      |
| regex_compile  | 76.8 ms                                                                                                                | 83.7 ms: 1.09x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.06x slower                                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.42 sec                                                                                                               | 1.20 sec: 1.19x faster                                                                                                     |
| pickle_dict          | 19.0 us                                                                                                                | 17.4 us: 1.09x faster                                                                                                      |
| pickle_pure_python   | 179 us                                                                                                                 | 173 us: 1.03x faster                                                                                                       |
| xml_etree_iterparse  | 63.3 ms                                                                                                                | 61.8 ms: 1.02x faster                                                                                                      |
| xml_etree_process    | 36.8 ms                                                                                                                | 36.2 ms: 1.01x faster                                                                                                      |
| xml_etree_generate   | 53.3 ms                                                                                                                | 52.6 ms: 1.01x faster                                                                                                      |
| pickle               | 7.44 us                                                                                                                | 7.36 us: 1.01x faster                                                                                                      |
| unpickle_pure_python | 127 us                                                                                                                 | 126 us: 1.01x faster                                                                                                       |
| json_dumps           | 5.61 ms                                                                                                                | 5.59 ms: 1.00x faster                                                                                                      |
| unpickle_list        | 2.69 us                                                                                                                | 2.78 us: 1.03x slower                                                                                                      |
| unpickle             | 8.39 us                                                                                                                | 8.67 us: 1.03x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.02x faster                                                                                                               |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.7 ms                                                                                                                | 20.8 ms: 1.12x slower                                                                                                      |
| python_startup         | 20.2 ms                                                                                                                | 23.2 ms: 1.15x slower                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.13x slower                                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.23 ms                                                                                                                | 5.71 ms: 1.09x faster                                                                                                      |
| genshi_text     | 15.8 ms                                                                                                                | 15.1 ms: 1.04x faster                                                                                                      |
| django_template | 21.7 ms                                                                                                                | 23.2 ms: 1.07x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody                    | 68.6 ms                                                                                                                | 57.0 ms: 1.20x faster                                                                                                      |
| spectral_norm            | 61.2 ms                                                                                                                | 50.9 ms: 1.20x faster                                                                                                      |
| tomli_loads              | 1.42 sec                                                                                                               | 1.20 sec: 1.19x faster                                                                                                     |
| float                    | 52.7 ms                                                                                                                | 46.2 ms: 1.14x faster                                                                                                      |
| fannkuch                 | 244 ms                                                                                                                 | 222 ms: 1.10x faster                                                                                                       |
| generators               | 22.4 ms                                                                                                                | 20.4 ms: 1.10x faster                                                                                                      |
| mako                     | 6.23 ms                                                                                                                | 5.71 ms: 1.09x faster                                                                                                      |
| pickle_dict              | 19.0 us                                                                                                                | 17.4 us: 1.09x faster                                                                                                      |
| asyncio_tcp_ssl          | 1.81 sec                                                                                                               | 1.67 sec: 1.09x faster                                                                                                     |
| scimark_sparse_mat_mult  | 2.40 ms                                                                                                                | 2.23 ms: 1.08x faster                                                                                                      |
| deepcopy_reduce          | 2.06 us                                                                                                                | 1.94 us: 1.06x faster                                                                                                      |
| genshi_text              | 15.8 ms                                                                                                                | 15.1 ms: 1.04x faster                                                                                                      |
| deepcopy                 | 227 us                                                                                                                 | 219 us: 1.04x faster                                                                                                       |
| deepcopy_memo            | 21.9 us                                                                                                                | 21.2 us: 1.04x faster                                                                                                      |
| chameleon                | 4.74 ms                                                                                                                | 4.58 ms: 1.03x faster                                                                                                      |
| pickle_pure_python       | 179 us                                                                                                                 | 173 us: 1.03x faster                                                                                                       |
| logging_simple           | 6.14 us                                                                                                                | 5.96 us: 1.03x faster                                                                                                      |
| pprint_pformat           | 1.00 sec                                                                                                               | 975 ms: 1.03x faster                                                                                                       |
| pprint_safe_repr         | 489 ms                                                                                                                 | 476 ms: 1.03x faster                                                                                                       |
| xml_etree_iterparse      | 63.3 ms                                                                                                                | 61.8 ms: 1.02x faster                                                                                                      |
| logging_format           | 6.49 us                                                                                                                | 6.39 us: 1.02x faster                                                                                                      |
| xml_etree_process        | 36.8 ms                                                                                                                | 36.2 ms: 1.01x faster                                                                                                      |
| html5lib                 | 36.3 ms                                                                                                                | 35.8 ms: 1.01x faster                                                                                                      |
| xml_etree_generate       | 53.3 ms                                                                                                                | 52.6 ms: 1.01x faster                                                                                                      |
| scimark_fft              | 171 ms                                                                                                                 | 169 ms: 1.01x faster                                                                                                       |
| coverage                 | 46.9 ms                                                                                                                | 46.4 ms: 1.01x faster                                                                                                      |
| sqlite_synth             | 1.61 us                                                                                                                | 1.59 us: 1.01x faster                                                                                                      |
| logging_silent           | 55.4 ns                                                                                                                | 54.8 ns: 1.01x faster                                                                                                      |
| pickle                   | 7.44 us                                                                                                                | 7.36 us: 1.01x faster                                                                                                      |
| typing_runtime_protocols | 70.7 us                                                                                                                | 69.9 us: 1.01x faster                                                                                                      |
| unpickle_pure_python     | 127 us                                                                                                                 | 126 us: 1.01x faster                                                                                                       |
| json                     | 2.92 ms                                                                                                                | 2.90 ms: 1.01x faster                                                                                                      |
| json_dumps               | 5.61 ms                                                                                                                | 5.59 ms: 1.00x faster                                                                                                      |
| pyflate                  | 284 ms                                                                                                                 | 283 ms: 1.00x faster                                                                                                       |
| chaos                    | 39.1 ms                                                                                                                | 39.3 ms: 1.01x slower                                                                                                      |
| gc_traversal             | 1.46 ms                                                                                                                | 1.48 ms: 1.01x slower                                                                                                      |
| async_tree_cpu_io_mixed  | 381 ms                                                                                                                 | 386 ms: 1.01x slower                                                                                                       |
| meteor_contest           | 72.9 ms                                                                                                                | 74.2 ms: 1.02x slower                                                                                                      |
| coroutines               | 13.3 ms                                                                                                                | 13.5 ms: 1.02x slower                                                                                                      |
| aiohttp                  | 881 us                                                                                                                 | 899 us: 1.02x slower                                                                                                       |
| pycparser                | 663 ms                                                                                                                 | 676 ms: 1.02x slower                                                                                                       |
| regex_effbot             | 1.57 ms                                                                                                                | 1.60 ms: 1.02x slower                                                                                                      |
| pidigits                 | 147 ms                                                                                                                 | 150 ms: 1.02x slower                                                                                                       |
| sqlglot_normalize        | 179 ms                                                                                                                 | 183 ms: 1.02x slower                                                                                                       |
| create_gc_cycles         | 717 us                                                                                                                 | 733 us: 1.02x slower                                                                                                       |
| tornado_http             | 83.2 ms                                                                                                                | 85.1 ms: 1.02x slower                                                                                                      |
| richards_super           | 30.7 ms                                                                                                                | 31.5 ms: 1.02x slower                                                                                                      |
| richards                 | 27.3 ms                                                                                                                | 28.0 ms: 1.02x slower                                                                                                      |
| sqlglot_parse            | 761 us                                                                                                                 | 783 us: 1.03x slower                                                                                                       |
| sqlglot_transpile        | 972 us                                                                                                                 | 1.00 ms: 1.03x slower                                                                                                      |
| unpickle_list            | 2.69 us                                                                                                                | 2.78 us: 1.03x slower                                                                                                      |
| unpickle                 | 8.39 us                                                                                                                | 8.67 us: 1.03x slower                                                                                                      |
| sympy_expand             | 274 ms                                                                                                                 | 284 ms: 1.03x slower                                                                                                       |
| bench_thread_pool        | 807 us                                                                                                                 | 837 us: 1.04x slower                                                                                                       |
| sympy_str                | 159 ms                                                                                                                 | 165 ms: 1.04x slower                                                                                                       |
| docutils                 | 1.62 sec                                                                                                               | 1.68 sec: 1.04x slower                                                                                                     |
| regex_dna                | 116 ms                                                                                                                 | 121 ms: 1.04x slower                                                                                                       |
| scimark_sor              | 77.7 ms                                                                                                                | 81.3 ms: 1.05x slower                                                                                                      |
| sqlglot_optimize         | 33.8 ms                                                                                                                | 35.4 ms: 1.05x slower                                                                                                      |
| 2to3                     | 210 ms                                                                                                                 | 220 ms: 1.05x slower                                                                                                       |
| deltablue                | 1.98 ms                                                                                                                | 2.08 ms: 1.05x slower                                                                                                      |
| sympy_sum                | 83.5 ms                                                                                                                | 87.9 ms: 1.05x slower                                                                                                      |
| nqueens                  | 57.6 ms                                                                                                                | 60.7 ms: 1.05x slower                                                                                                      |
| mypy2                    | 436 ms                                                                                                                 | 462 ms: 1.06x slower                                                                                                       |
| scimark_monte_carlo      | 38.9 ms                                                                                                                | 41.3 ms: 1.06x slower                                                                                                      |
| django_template          | 21.7 ms                                                                                                                | 23.2 ms: 1.07x slower                                                                                                      |
| regex_v8                 | 14.3 ms                                                                                                                | 15.3 ms: 1.07x slower                                                                                                      |
| async_generators         | 227 ms                                                                                                                 | 244 ms: 1.07x slower                                                                                                       |
| sympy_integrate          | 12.3 ms                                                                                                                | 13.2 ms: 1.08x slower                                                                                                      |
| bench_mp_pool            | 63.6 ms                                                                                                                | 68.7 ms: 1.08x slower                                                                                                      |
| regex_compile            | 76.8 ms                                                                                                                | 83.7 ms: 1.09x slower                                                                                                      |
| go                       | 84.5 ms                                                                                                                | 92.6 ms: 1.10x slower                                                                                                      |
| thrift                   | 8.04 ms                                                                                                                | 8.86 ms: 1.10x slower                                                                                                      |
| raytrace                 | 163 ms                                                                                                                 | 181 ms: 1.11x slower                                                                                                       |
| python_startup_no_site   | 18.7 ms                                                                                                                | 20.8 ms: 1.12x slower                                                                                                      |
| mdp                      | 1.38 sec                                                                                                               | 1.55 sec: 1.12x slower                                                                                                     |
| python_startup           | 20.2 ms                                                                                                                | 23.2 ms: 1.15x slower                                                                                                      |
| hexiom                   | 3.78 ms                                                                                                                | 4.37 ms: 1.16x slower                                                                                                      |
| unpack_sequence          | 37.3 ns                                                                                                                | 47.7 ns: 1.28x slower                                                                                                      |
| scimark_lu               | 54.4 ms                                                                                                                | 70.4 ms: 1.29x slower                                                                                                      |
| Geometric mean           | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (18): async_tree_memoization, json_loads, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, pathlib, asyncio_tcp, async_tree_io_tg, async_tree_none_tg, async_tree_none, xml_etree_parse, telco, dulwich_log, crypto_pyaes, async_tree_io, comprehensions, pickle_list, genshi_xml, pylint


# HPT report

- Reliability score: 98.49% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: unknown