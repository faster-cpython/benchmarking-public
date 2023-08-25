
# Results vs. 3.11.0

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: 00b5a0c
- commit date: 2023-01-27
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.42 ms: 1.01x faster                                                  |
| docutils       | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                 |
| html5lib       | 64.5 ms                                                | 60.6 ms: 1.06x faster                                                  |
| tornado_http   | 96.3 ms                                                | 94.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.5 ms: 1.07x faster                                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| nbody          | 93.1 ms                                                | 94.8 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.37 ms: 1.18x faster                                                  |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| regex_v8       | 22.0 ms                                                | 21.5 ms: 1.03x faster                                                  |
| regex_dna      | 204 ms                                                 | 205 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.32 ms: 1.35x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.14x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 146 ms: 1.08x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 285 us: 1.07x faster                                                   |
| unpickle             | 13.7 us                                                | 13.0 us: 1.05x faster                                                  |
| json_loads           | 26.5 us                                                | 25.7 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.01x faster                                                   |
| xml_etree_process    | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                  |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.01x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.15 us: 1.01x slower                                                  |
| unpickle_list        | 4.91 us                                                | 4.95 us: 1.01x slower                                                  |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 77.8 ms: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.96 ms: 1.05x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.7 ms: 1.11x faster                                                  |
| mako            | 10.1 ms                                                | 9.45 ms: 1.07x faster                                                  |
| genshi_text     | 21.6 ms                                                | 20.4 ms: 1.06x faster                                                  |
| django_template | 32.6 ms                                                | 33.3 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 498 ms: 1.85x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.32 ms: 1.35x faster                                                  |
| regex_effbot            | 3.99 ms                                                | 3.37 ms: 1.18x faster                                                  |
| gc_traversal            | 4.02 ms                                                | 3.41 ms: 1.18x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.14x faster                                                   |
| deltablue               | 3.67 ms                                                | 3.25 ms: 1.13x faster                                                  |
| genshi_xml              | 51.8 ms                                                | 46.7 ms: 1.11x faster                                                  |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                                   |
| logging_silent          | 101 ns                                                 | 92.0 ns: 1.10x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 33.8 us: 1.10x faster                                                  |
| nqueens                 | 83.4 ms                                                | 76.3 ms: 1.09x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 146 ms: 1.08x faster                                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.17 ms: 1.08x faster                                                  |
| richards                | 45.7 ms                                                | 42.4 ms: 1.08x faster                                                  |
| aiohttp                 | 1.10 ms                                                | 1.02 ms: 1.08x faster                                                  |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| pickle_pure_python      | 306 us                                                 | 285 us: 1.07x faster                                                   |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                                   |
| gunicorn                | 1.18 ms                                                | 1.10 ms: 1.07x faster                                                  |
| mako                    | 10.1 ms                                                | 9.45 ms: 1.07x faster                                                  |
| hexiom                  | 6.37 ms                                                | 5.98 ms: 1.07x faster                                                  |
| float                   | 77.2 ms                                                | 72.5 ms: 1.07x faster                                                  |
| html5lib                | 64.5 ms                                                | 60.6 ms: 1.06x faster                                                  |
| sympy_str               | 290 ms                                                 | 273 ms: 1.06x faster                                                   |
| pyflate                 | 418 ms                                                 | 394 ms: 1.06x faster                                                   |
| mdp                     | 2.62 sec                                               | 2.47 sec: 1.06x faster                                                 |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                 |
| genshi_text             | 21.6 ms                                                | 20.4 ms: 1.06x faster                                                  |
| scimark_fft             | 328 ms                                                 | 311 ms: 1.05x faster                                                   |
| telco                   | 6.58 ms                                                | 6.25 ms: 1.05x faster                                                  |
| unpickle                | 13.7 us                                                | 13.0 us: 1.05x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                 |
| spectral_norm           | 100 ms                                                 | 95.4 ms: 1.05x faster                                                  |
| raytrace                | 297 ms                                                 | 283 ms: 1.05x faster                                                   |
| async_generators        | 368 ms                                                 | 352 ms: 1.05x faster                                                   |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| docutils                | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                 |
| pprint_safe_repr        | 701 ms                                                 | 671 ms: 1.05x faster                                                   |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                                   |
| logging_format          | 6.68 us                                                | 6.45 us: 1.04x faster                                                  |
| json                    | 4.94 ms                                                | 4.78 ms: 1.03x faster                                                  |
| sympy_expand            | 475 ms                                                 | 461 ms: 1.03x faster                                                   |
| json_loads              | 26.5 us                                                | 25.7 us: 1.03x faster                                                  |
| chaos                   | 69.2 ms                                                | 67.2 ms: 1.03x faster                                                  |
| logging_simple          | 6.03 us                                                | 5.87 us: 1.03x faster                                                  |
| regex_v8                | 22.0 ms                                                | 21.5 ms: 1.03x faster                                                  |
| crypto_pyaes            | 74.7 ms                                                | 73.1 ms: 1.02x faster                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 52.1 ms: 1.02x faster                                                  |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                                   |
| async_tree_none         | 526 ms                                                 | 517 ms: 1.02x faster                                                   |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                   |
| tornado_http            | 96.3 ms                                                | 94.7 ms: 1.02x faster                                                  |
| fannkuch                | 388 ms                                                 | 381 ms: 1.02x faster                                                   |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.02x faster                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 67.1 ms: 1.01x faster                                                  |
| dulwich_log             | 63.7 ms                                                | 62.7 ms: 1.01x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.01x faster                                                   |
| coroutines              | 25.5 ms                                                | 25.2 ms: 1.01x faster                                                  |
| go                      | 140 ms                                                 | 138 ms: 1.01x faster                                                   |
| thrift                  | 756 us                                                 | 749 us: 1.01x faster                                                   |
| chameleon               | 6.47 ms                                                | 6.42 ms: 1.01x faster                                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.92 us: 1.01x faster                                                  |
| xml_etree_process       | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                  |
| coverage                | 100 ms                                                 | 99.4 ms: 1.01x faster                                                  |
| regex_dna               | 204 ms                                                 | 205 ms: 1.00x slower                                                   |
| pickle_dict             | 31.1 us                                                | 31.3 us: 1.01x slower                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.15 us: 1.01x slower                                                  |
| unpickle_list           | 4.91 us                                                | 4.95 us: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 747 ms: 1.01x slower                                                   |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                  |
| unpack_sequence         | 43.1 ns                                                | 43.8 ns: 1.02x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                 |
| nbody                   | 93.1 ms                                                | 94.8 ms: 1.02x slower                                                  |
| django_template         | 32.6 ms                                                | 33.3 ms: 1.02x slower                                                  |
| scimark_lu              | 110 ms                                                 | 112 ms: 1.02x slower                                                   |
| xml_etree_generate      | 76.2 ms                                                | 77.8 ms: 1.02x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                  |
| async_tree_memoization  | 627 ms                                                 | 646 ms: 1.03x slower                                                   |
| djangocms               | 32.4 us                                                | 33.5 us: 1.03x slower                                                  |
| python_startup          | 8.52 ms                                                | 8.96 ms: 1.05x slower                                                  |
| generators              | 73.5 ms                                                | 78.4 ms: 1.07x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.66 ms: 1.12x slower                                                  |
| bench_thread_pool       | 819 us                                                 | 963 us: 1.18x slower                                                   |
| bench_mp_pool           | 24.0 ms                                                | 30.6 ms: 1.27x slower                                                  |
| dask                    | 360 ms                                                 | 518 ms: 1.44x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (2): sqlglot_normalize, sqlglot_transpile
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230127-3.12.0a4+-00b5a0c/bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
