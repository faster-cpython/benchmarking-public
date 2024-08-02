# Results vs. base

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-amd64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.03x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 208 ms                                                                                                                 | 231 ms: 1.11x slower                                                                                                       |
| chameleon      | 4.81 ms                                                                                                                | 4.96 ms: 1.03x slower                                                                                                      |
| docutils       | 1.62 sec                                                                                                               | 1.77 sec: 1.09x slower                                                                                                     |
| html5lib       | 35.5 ms                                                                                                                | 36.5 ms: 1.03x slower                                                                                                      |
| tornado_http   | 82.1 ms                                                                                                                | 86.3 ms: 1.05x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.06x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                                                                                 | 620 ms: 1.03x slower                                                                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                                                                                 | 400 ms: 1.03x slower                                                                                                       |
| async_tree_memoization    | 265 ms                                                                                                                 | 276 ms: 1.04x slower                                                                                                       |
| async_tree_none           | 217 ms                                                                                                                 | 226 ms: 1.04x slower                                                                                                       |
| async_tree_none_tg        | 204 ms                                                                                                                 | 214 ms: 1.05x slower                                                                                                       |
| async_tree_memoization_tg | 258 ms                                                                                                                 | 273 ms: 1.06x slower                                                                                                       |
| Geometric mean            | (ref)                                                                                                                  | 1.04x slower                                                                                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 64.9 ms                                                                                                                | 50.4 ms: 1.29x faster                                                                                                      |
| float          | 50.1 ms                                                                                                                | 44.3 ms: 1.13x faster                                                                                                      |
| pidigits       | 150 ms                                                                                                                 | 149 ms: 1.00x faster                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.13x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 1.57 ms                                                                                                                | 1.59 ms: 1.01x slower                                                                                                      |
| regex_dna      | 119 ms                                                                                                                 | 120 ms: 1.01x slower                                                                                                       |
| regex_compile  | 78.1 ms                                                                                                                | 88.0 ms: 1.13x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                                                                               | 1.23 sec: 1.11x faster                                                                                                     |
| pickle_dict          | 18.3 us                                                                                                                | 17.6 us: 1.04x faster                                                                                                      |
| pickle_list          | 2.89 us                                                                                                                | 2.80 us: 1.04x faster                                                                                                      |
| xml_etree_generate   | 53.8 ms                                                                                                                | 52.4 ms: 1.03x faster                                                                                                      |
| xml_etree_iterparse  | 62.9 ms                                                                                                                | 61.4 ms: 1.02x faster                                                                                                      |
| xml_etree_parse      | 92.1 ms                                                                                                                | 90.7 ms: 1.01x faster                                                                                                      |
| unpickle             | 8.45 us                                                                                                                | 8.50 us: 1.01x slower                                                                                                      |
| json_loads           | 14.1 us                                                                                                                | 14.3 us: 1.01x slower                                                                                                      |
| unpickle_pure_python | 124 us                                                                                                                 | 126 us: 1.02x slower                                                                                                       |
| json_dumps           | 5.60 ms                                                                                                                | 5.77 ms: 1.03x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_process, unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.6 ms                                                                                                                | 17.8 ms: 1.07x slower                                                                                                      |
| python_startup         | 20.2 ms                                                                                                                | 21.9 ms: 1.08x slower                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.08x slower                                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.41 ms                                                                                                                | 5.07 ms: 1.27x faster                                                                                                      |
| django_template | 22.6 ms                                                                                                                | 25.6 ms: 1.13x slower                                                                                                      |
| genshi_text     | 14.7 ms                                                                                                                | 18.3 ms: 1.25x slower                                                                                                      |
| genshi_xml      | 31.8 ms                                                                                                                | 44.6 ms: 1.40x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.12x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                 | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm             | 63.4 ms                                                                                                                | 44.4 ms: 1.43x faster                                                                                                      |
| nbody                     | 64.9 ms                                                                                                                | 50.4 ms: 1.29x faster                                                                                                      |
| mako                      | 6.41 ms                                                                                                                | 5.07 ms: 1.27x faster                                                                                                      |
| fannkuch                  | 244 ms                                                                                                                 | 211 ms: 1.16x faster                                                                                                       |
| scimark_fft               | 170 ms                                                                                                                 | 148 ms: 1.15x faster                                                                                                       |
| float                     | 50.1 ms                                                                                                                | 44.3 ms: 1.13x faster                                                                                                      |
| scimark_sparse_mat_mult   | 2.40 ms                                                                                                                | 2.14 ms: 1.12x faster                                                                                                      |
| tomli_loads               | 1.37 sec                                                                                                               | 1.23 sec: 1.11x faster                                                                                                     |
| deepcopy_memo             | 22.0 us                                                                                                                | 20.1 us: 1.09x faster                                                                                                      |
| crypto_pyaes              | 45.0 ms                                                                                                                | 41.4 ms: 1.09x faster                                                                                                      |
| pyflate                   | 278 ms                                                                                                                 | 257 ms: 1.08x faster                                                                                                       |
| telco                     | 4.68 ms                                                                                                                | 4.49 ms: 1.04x faster                                                                                                      |
| pickle_dict               | 18.3 us                                                                                                                | 17.6 us: 1.04x faster                                                                                                      |
| pickle_list               | 2.89 us                                                                                                                | 2.80 us: 1.04x faster                                                                                                      |
| xml_etree_generate        | 53.8 ms                                                                                                                | 52.4 ms: 1.03x faster                                                                                                      |
| xml_etree_iterparse       | 62.9 ms                                                                                                                | 61.4 ms: 1.02x faster                                                                                                      |
| pprint_pformat            | 965 ms                                                                                                                 | 947 ms: 1.02x faster                                                                                                       |
| pprint_safe_repr          | 471 ms                                                                                                                 | 462 ms: 1.02x faster                                                                                                       |
| scimark_monte_carlo       | 40.1 ms                                                                                                                | 39.4 ms: 1.02x faster                                                                                                      |
| xml_etree_parse           | 92.1 ms                                                                                                                | 90.7 ms: 1.01x faster                                                                                                      |
| sqlite_synth              | 1.60 us                                                                                                                | 1.58 us: 1.01x faster                                                                                                      |
| comprehensions            | 10.4 us                                                                                                                | 10.2 us: 1.01x faster                                                                                                      |
| pidigits                  | 150 ms                                                                                                                 | 149 ms: 1.00x faster                                                                                                       |
| unpickle                  | 8.45 us                                                                                                                | 8.50 us: 1.01x slower                                                                                                      |
| regex_effbot              | 1.57 ms                                                                                                                | 1.59 ms: 1.01x slower                                                                                                      |
| regex_dna                 | 119 ms                                                                                                                 | 120 ms: 1.01x slower                                                                                                       |
| json_loads                | 14.1 us                                                                                                                | 14.3 us: 1.01x slower                                                                                                      |
| logging_format            | 6.17 us                                                                                                                | 6.24 us: 1.01x slower                                                                                                      |
| logging_simple            | 5.69 us                                                                                                                | 5.78 us: 1.01x slower                                                                                                      |
| meteor_contest            | 71.8 ms                                                                                                                | 72.8 ms: 1.01x slower                                                                                                      |
| unpickle_pure_python      | 124 us                                                                                                                 | 126 us: 1.02x slower                                                                                                       |
| async_tree_io_tg          | 605 ms                                                                                                                 | 620 ms: 1.03x slower                                                                                                       |
| create_gc_cycles          | 900 us                                                                                                                 | 924 us: 1.03x slower                                                                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                                                                                 | 400 ms: 1.03x slower                                                                                                       |
| html5lib                  | 35.5 ms                                                                                                                | 36.5 ms: 1.03x slower                                                                                                      |
| json_dumps                | 5.60 ms                                                                                                                | 5.77 ms: 1.03x slower                                                                                                      |
| chameleon                 | 4.81 ms                                                                                                                | 4.96 ms: 1.03x slower                                                                                                      |
| mdp                       | 1.37 sec                                                                                                               | 1.41 sec: 1.03x slower                                                                                                     |
| json                      | 2.94 ms                                                                                                                | 3.04 ms: 1.03x slower                                                                                                      |
| aiohttp                   | 898 us                                                                                                                 | 929 us: 1.03x slower                                                                                                       |
| chaos                     | 37.9 ms                                                                                                                | 39.3 ms: 1.04x slower                                                                                                      |
| async_tree_memoization    | 265 ms                                                                                                                 | 276 ms: 1.04x slower                                                                                                       |
| async_tree_none           | 217 ms                                                                                                                 | 226 ms: 1.04x slower                                                                                                       |
| bench_thread_pool         | 787 us                                                                                                                 | 824 us: 1.05x slower                                                                                                       |
| richards                  | 27.3 ms                                                                                                                | 28.6 ms: 1.05x slower                                                                                                      |
| richards_super            | 30.8 ms                                                                                                                | 32.3 ms: 1.05x slower                                                                                                      |
| async_tree_none_tg        | 204 ms                                                                                                                 | 214 ms: 1.05x slower                                                                                                       |
| tornado_http              | 82.1 ms                                                                                                                | 86.3 ms: 1.05x slower                                                                                                      |
| async_tree_memoization_tg | 258 ms                                                                                                                 | 273 ms: 1.06x slower                                                                                                       |
| deepcopy_reduce           | 1.98 us                                                                                                                | 2.09 us: 1.06x slower                                                                                                      |
| nqueens                   | 55.9 ms                                                                                                                | 59.1 ms: 1.06x slower                                                                                                      |
| sqlglot_parse             | 755 us                                                                                                                 | 800 us: 1.06x slower                                                                                                       |
| dulwich_log               | 38.2 ms                                                                                                                | 40.5 ms: 1.06x slower                                                                                                      |
| bench_mp_pool             | 65.0 ms                                                                                                                | 69.4 ms: 1.07x slower                                                                                                      |
| python_startup_no_site    | 16.6 ms                                                                                                                | 17.8 ms: 1.07x slower                                                                                                      |
| sqlglot_transpile         | 964 us                                                                                                                 | 1.03 ms: 1.07x slower                                                                                                      |
| logging_silent            | 52.6 ns                                                                                                                | 56.5 ns: 1.07x slower                                                                                                      |
| coverage                  | 43.3 ms                                                                                                                | 46.8 ms: 1.08x slower                                                                                                      |
| deepcopy                  | 218 us                                                                                                                 | 237 us: 1.08x slower                                                                                                       |
| python_startup            | 20.2 ms                                                                                                                | 21.9 ms: 1.08x slower                                                                                                      |
| typing_runtime_protocols  | 102 us                                                                                                                 | 111 us: 1.09x slower                                                                                                       |
| docutils                  | 1.62 sec                                                                                                               | 1.77 sec: 1.09x slower                                                                                                     |
| scimark_sor               | 73.9 ms                                                                                                                | 81.1 ms: 1.10x slower                                                                                                      |
| sympy_sum                 | 85.3 ms                                                                                                                | 93.9 ms: 1.10x slower                                                                                                      |
| generators                | 19.4 ms                                                                                                                | 21.5 ms: 1.10x slower                                                                                                      |
| 2to3                      | 208 ms                                                                                                                 | 231 ms: 1.11x slower                                                                                                       |
| async_generators          | 225 ms                                                                                                                 | 249 ms: 1.11x slower                                                                                                       |
| sqlglot_optimize          | 32.8 ms                                                                                                                | 36.7 ms: 1.12x slower                                                                                                      |
| sympy_str                 | 160 ms                                                                                                                 | 179 ms: 1.12x slower                                                                                                       |
| go                        | 83.4 ms                                                                                                                | 93.6 ms: 1.12x slower                                                                                                      |
| regex_compile             | 78.1 ms                                                                                                                | 88.0 ms: 1.13x slower                                                                                                      |
| raytrace                  | 159 ms                                                                                                                 | 180 ms: 1.13x slower                                                                                                       |
| django_template           | 22.6 ms                                                                                                                | 25.6 ms: 1.13x slower                                                                                                      |
| sympy_expand              | 272 ms                                                                                                                 | 312 ms: 1.15x slower                                                                                                       |
| pylint                    | 205 ms                                                                                                                 | 235 ms: 1.15x slower                                                                                                       |
| thrift                    | 7.90 ms                                                                                                                | 9.10 ms: 1.15x slower                                                                                                      |
| sympy_integrate           | 12.3 ms                                                                                                                | 14.1 ms: 1.15x slower                                                                                                      |
| mypy2                     | 418 ms                                                                                                                 | 484 ms: 1.16x slower                                                                                                       |
| genshi_text               | 14.7 ms                                                                                                                | 18.3 ms: 1.25x slower                                                                                                      |
| hexiom                    | 3.71 ms                                                                                                                | 4.66 ms: 1.26x slower                                                                                                      |
| deltablue                 | 1.88 ms                                                                                                                | 2.37 ms: 1.26x slower                                                                                                      |
| scimark_lu                | 54.7 ms                                                                                                                | 69.0 ms: 1.26x slower                                                                                                      |
| genshi_xml                | 31.8 ms                                                                                                                | 44.6 ms: 1.40x slower                                                                                                      |
| Geometric mean            | (ref)                                                                                                                  | 1.03x slower                                                                                                               |

Benchmark hidden because not significant (14): regex_v8, pycparser, asyncio_tcp, pickle_pure_python, xml_etree_process, flaskblogging, asyncio_tcp_ssl, unpickle_list, pickle, pathlib, gc_traversal, coroutines, async_tree_cpu_io_mixed_tg, async_tree_io
Ignored benchmarks (1) of results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: sqlglot_normalize

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown