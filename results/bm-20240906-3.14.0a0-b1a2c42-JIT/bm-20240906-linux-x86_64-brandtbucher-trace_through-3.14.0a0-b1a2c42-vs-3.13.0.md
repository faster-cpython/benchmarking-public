# Results vs. 3.13.0

- fork: brandtbucher
- ref: trace_through
- machine: linux-x86_64
- commit hash: b1a2c42
- commit date: 2024-09-06
- overall geometric mean: 1.00x slower
- HPT reliability: 78.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 278 ms: 1.05x slower                                                 |
| docutils       | 2.58 sec                                               | 3.00 sec: 1.16x slower                                               |
| html5lib       | 64.5 ms                                                | 62.4 ms: 1.03x faster                                                |
| tornado_http   | 91.5 ms                                                | 95.7 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 401 ms: 1.16x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 402 ms: 1.10x faster                                                 |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                 |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 562 ms: 1.02x faster                                                 |
| asyncio_tcp               | 488 ms                                                 | 485 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                               |
| coroutines                | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                |
| async_generators          | 433 ms                                                 | 460 ms: 1.06x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 889 ms: 1.08x slower                                                 |
| async_tree_io             | 843 ms                                                 | 926 ms: 1.10x slower                                                 |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.3 ms: 1.12x faster                                                |
| nbody          | 85.7 ms                                                | 81.0 ms: 1.06x faster                                                |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.47 ms: 1.12x faster                                                |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                |
| regex_compile  | 131 ms                                                 | 145 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate  | 87.0 ms                                                | 76.5 ms: 1.14x faster                                                |
| xml_etree_process   | 60.4 ms                                                | 54.0 ms: 1.12x faster                                                |
| tomli_loads         | 2.11 sec                                               | 1.95 sec: 1.08x faster                                               |
| xml_etree_parse     | 156 ms                                                 | 145 ms: 1.07x faster                                                 |
| xml_etree_iterparse | 102 ms                                                 | 98.5 ms: 1.04x faster                                                |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                |
| pickle              | 11.6 us                                                | 11.7 us: 1.01x slower                                                |
| pickle_list         | 5.01 us                                                | 5.09 us: 1.02x slower                                                |
| pickle_dict         | 33.2 us                                                | 34.5 us: 1.04x slower                                                |
| unpickle_list       | 4.96 us                                                | 5.16 us: 1.04x slower                                                |
| json_loads          | 27.0 us                                                | 28.7 us: 1.06x slower                                                |
| Geometric mean      | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (3): unpickle_pure_python, pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                |
| django_template | 34.4 ms                                                | 36.6 ms: 1.06x slower                                                |
| genshi_text     | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                |
| genshi_xml      | 50.3 ms                                                | 55.9 ms: 1.11x slower                                                |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.4 us: 1.44x faster                                                |
| deepcopy                  | 352 us                                                 | 264 us: 1.33x faster                                                 |
| richards_super            | 54.4 ms                                                | 44.0 ms: 1.24x faster                                                |
| deepcopy_reduce           | 3.17 us                                                | 2.62 us: 1.21x faster                                                |
| richards                  | 48.1 ms                                                | 39.8 ms: 1.21x faster                                                |
| scimark_fft               | 369 ms                                                 | 316 ms: 1.17x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 401 ms: 1.16x faster                                                 |
| spectral_norm             | 115 ms                                                 | 100 ms: 1.15x faster                                                 |
| xml_etree_generate        | 87.0 ms                                                | 76.5 ms: 1.14x faster                                                |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.43 ms: 1.13x faster                                                |
| mako                      | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                |
| xml_etree_process         | 60.4 ms                                                | 54.0 ms: 1.12x faster                                                |
| regex_effbot              | 3.88 ms                                                | 3.47 ms: 1.12x faster                                                |
| float                     | 78.5 ms                                                | 70.3 ms: 1.12x faster                                                |
| async_tree_memoization    | 442 ms                                                 | 402 ms: 1.10x faster                                                 |
| crypto_pyaes              | 73.0 ms                                                | 66.7 ms: 1.09x faster                                                |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 1.95 sec: 1.08x faster                                               |
| pathlib                   | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.07x faster                                                 |
| gc_traversal              | 3.81 ms                                                | 3.59 ms: 1.06x faster                                                |
| nbody                     | 85.7 ms                                                | 81.0 ms: 1.06x faster                                                |
| scimark_monte_carlo       | 66.3 ms                                                | 62.7 ms: 1.06x faster                                                |
| telco                     | 8.45 ms                                                | 7.99 ms: 1.06x faster                                                |
| go                        | 142 ms                                                 | 134 ms: 1.05x faster                                                 |
| scimark_sor               | 122 ms                                                 | 116 ms: 1.05x faster                                                 |
| sqlite_synth              | 2.85 us                                                | 2.72 us: 1.05x faster                                                |
| bpe_tokeniser             | 4.69 sec                                               | 4.50 sec: 1.04x faster                                               |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                 |
| pprint_safe_repr          | 744 ms                                                 | 716 ms: 1.04x faster                                                 |
| regex_dna                 | 220 ms                                                 | 212 ms: 1.04x faster                                                 |
| xml_etree_iterparse       | 102 ms                                                 | 98.5 ms: 1.04x faster                                                |
| regex_v8                  | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                |
| html5lib                  | 64.5 ms                                                | 62.4 ms: 1.03x faster                                                |
| pyflate                   | 460 ms                                                 | 449 ms: 1.02x faster                                                 |
| thrift                    | 796 us                                                 | 780 us: 1.02x faster                                                 |
| logging_silent            | 102 ns                                                 | 100.0 ns: 1.02x faster                                               |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 562 ms: 1.02x faster                                                 |
| pprint_pformat            | 1.51 sec                                               | 1.48 sec: 1.02x faster                                               |
| fannkuch                  | 381 ms                                                 | 374 ms: 1.02x faster                                                 |
| scimark_lu                | 115 ms                                                 | 113 ms: 1.02x faster                                                 |
| deltablue                 | 3.15 ms                                                | 3.11 ms: 1.01x faster                                                |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                |
| mdp                       | 2.74 sec                                               | 2.72 sec: 1.01x faster                                               |
| asyncio_tcp               | 488 ms                                                 | 485 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                               |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                 |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                |
| pickle                    | 11.6 us                                                | 11.7 us: 1.01x slower                                                |
| meteor_contest            | 108 ms                                                 | 109 ms: 1.01x slower                                                 |
| pickle_list               | 5.01 us                                                | 5.09 us: 1.02x slower                                                |
| json                      | 5.20 ms                                                | 5.30 ms: 1.02x slower                                                |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                |
| coroutines                | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                |
| bench_thread_pool         | 815 us                                                 | 834 us: 1.02x slower                                                 |
| coverage                  | 83.7 ms                                                | 85.8 ms: 1.02x slower                                                |
| python_startup_no_site    | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                |
| pickle_dict               | 33.2 us                                                | 34.5 us: 1.04x slower                                                |
| unpickle_list             | 4.96 us                                                | 5.16 us: 1.04x slower                                                |
| tornado_http              | 91.5 ms                                                | 95.7 ms: 1.05x slower                                                |
| raytrace                  | 262 ms                                                 | 274 ms: 1.05x slower                                                 |
| 2to3                      | 265 ms                                                 | 278 ms: 1.05x slower                                                 |
| typing_runtime_protocols  | 159 us                                                 | 167 us: 1.05x slower                                                 |
| sqlglot_normalize         | 107 ms                                                 | 113 ms: 1.05x slower                                                 |
| sqlglot_parse             | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                |
| sqlglot_transpile         | 1.57 ms                                                | 1.67 ms: 1.06x slower                                                |
| json_loads                | 27.0 us                                                | 28.7 us: 1.06x slower                                                |
| django_template           | 34.4 ms                                                | 36.6 ms: 1.06x slower                                                |
| async_generators          | 433 ms                                                 | 460 ms: 1.06x slower                                                 |
| nqueens                   | 80.6 ms                                                | 86.1 ms: 1.07x slower                                                |
| genshi_text               | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                |
| async_tree_io_tg          | 825 ms                                                 | 889 ms: 1.08x slower                                                 |
| sqlglot_optimize          | 53.9 ms                                                | 58.4 ms: 1.08x slower                                                |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.10x slower                                                |
| sympy_expand              | 462 ms                                                 | 507 ms: 1.10x slower                                                 |
| async_tree_io             | 843 ms                                                 | 926 ms: 1.10x slower                                                 |
| regex_compile             | 131 ms                                                 | 145 ms: 1.10x slower                                                 |
| genshi_xml                | 50.3 ms                                                | 55.9 ms: 1.11x slower                                                |
| sympy_str                 | 274 ms                                                 | 304 ms: 1.11x slower                                                 |
| dulwich_log               | 63.0 ms                                                | 70.7 ms: 1.12x slower                                                |
| generators                | 28.8 ms                                                | 33.0 ms: 1.15x slower                                                |
| sympy_integrate           | 19.9 ms                                                | 23.0 ms: 1.16x slower                                                |
| docutils                  | 2.58 sec                                               | 3.00 sec: 1.16x slower                                               |
| sympy_sum                 | 150 ms                                                 | 175 ms: 1.17x slower                                                 |
| pylint                    | 313 ms                                                 | 374 ms: 1.20x slower                                                 |
| hexiom                    | 6.13 ms                                                | 7.73 ms: 1.26x slower                                                |
| unpack_sequence           | 42.4 ns                                                | 139 ns: 3.27x slower                                                 |
| Geometric mean            | (ref)                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (10): pycparser, logging_format, async_tree_cpu_io_mixed_tg, unpickle_pure_python, asyncio_websockets, bench_mp_pool, logging_simple, chaos, pickle_pure_python, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 78.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x