
# Results vs. 3.11.0

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: f23eec9
- commit date: 2023-01-27
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.28 ms: 1.03x faster                                                  |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                 |
| html5lib       | 64.5 ms                                                | 60.2 ms: 1.07x faster                                                  |
| tornado_http   | 96.3 ms                                                | 93.9 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.7 ms: 1.08x faster                                                  |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                                   |
| nbody          | 93.1 ms                                                | 94.0 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.57 ms: 1.12x faster                                                  |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                   |
| regex_v8       | 22.0 ms                                                | 26.0 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.38 ms: 1.34x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                   |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                   |
| unpickle             | 13.7 us                                                | 13.1 us: 1.05x faster                                                  |
| pickle_list          | 4.11 us                                                | 4.03 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                                  |
| xml_etree_process    | 53.9 ms                                                | 53.7 ms: 1.00x faster                                                  |
| xml_etree_generate   | 76.2 ms                                                | 77.3 ms: 1.01x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.04 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.90 ms: 1.04x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.45 ms: 1.07x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.5 ms: 1.11x faster                                                  |
| genshi_text     | 21.6 ms                                                | 20.7 ms: 1.04x faster                                                  |
| mako            | 10.1 ms                                                | 9.71 ms: 1.04x faster                                                  |
| django_template | 32.6 ms                                                | 32.8 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 498 ms: 1.85x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.38 ms: 1.34x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                   |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.02 ms: 1.12x faster                                                  |
| regex_effbot            | 3.99 ms                                                | 3.57 ms: 1.12x faster                                                  |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.12x faster                                                   |
| genshi_xml              | 51.8 ms                                                | 46.5 ms: 1.11x faster                                                  |
| aiohttp                 | 1.10 ms                                                | 995 us: 1.11x faster                                                   |
| gunicorn                | 1.18 ms                                                | 1.06 ms: 1.11x faster                                                  |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                  |
| nqueens                 | 83.4 ms                                                | 76.3 ms: 1.09x faster                                                  |
| json                    | 4.94 ms                                                | 4.56 ms: 1.08x faster                                                  |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                                   |
| scimark_fft             | 328 ms                                                 | 303 ms: 1.08x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                   |
| logging_format          | 6.68 us                                                | 6.19 us: 1.08x faster                                                  |
| float                   | 77.2 ms                                                | 71.7 ms: 1.08x faster                                                  |
| richards                | 45.7 ms                                                | 42.5 ms: 1.08x faster                                                  |
| sympy_str               | 290 ms                                                 | 270 ms: 1.08x faster                                                   |
| logging_simple          | 6.03 us                                                | 5.62 us: 1.07x faster                                                  |
| html5lib                | 64.5 ms                                                | 60.2 ms: 1.07x faster                                                  |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.07x faster                                                   |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                                   |
| chaos                   | 69.2 ms                                                | 64.9 ms: 1.07x faster                                                  |
| logging_silent          | 101 ns                                                 | 94.9 ns: 1.07x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 34.8 us: 1.06x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.00 ms: 1.06x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 776 us: 1.05x faster                                                   |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                                   |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                 |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                 |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                   |
| pyflate                 | 418 ms                                                 | 399 ms: 1.05x faster                                                   |
| unpickle                | 13.7 us                                                | 13.1 us: 1.05x faster                                                  |
| async_generators        | 368 ms                                                 | 352 ms: 1.05x faster                                                   |
| coroutines              | 25.5 ms                                                | 24.5 ms: 1.04x faster                                                  |
| genshi_text             | 21.6 ms                                                | 20.7 ms: 1.04x faster                                                  |
| mako                    | 10.1 ms                                                | 9.71 ms: 1.04x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                 |
| sqlglot_optimize        | 53.1 ms                                                | 51.3 ms: 1.04x faster                                                  |
| pprint_safe_repr        | 701 ms                                                 | 678 ms: 1.04x faster                                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 65.8 ms: 1.03x faster                                                  |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                  |
| telco                   | 6.58 ms                                                | 6.39 ms: 1.03x faster                                                  |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| chameleon               | 6.47 ms                                                | 6.28 ms: 1.03x faster                                                  |
| coverage                | 100 ms                                                 | 97.2 ms: 1.03x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                   |
| tornado_http            | 96.3 ms                                                | 93.9 ms: 1.03x faster                                                  |
| deepcopy                | 342 us                                                 | 334 us: 1.03x faster                                                   |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.02x faster                                                   |
| crypto_pyaes            | 74.7 ms                                                | 73.0 ms: 1.02x faster                                                  |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                   |
| pickle_list             | 4.11 us                                                | 4.03 us: 1.02x faster                                                  |
| mdp                     | 2.62 sec                                               | 2.56 sec: 1.02x faster                                                 |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                  |
| dulwich_log             | 63.7 ms                                                | 62.6 ms: 1.02x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| pickle_dict             | 31.1 us                                                | 30.8 us: 1.01x faster                                                  |
| thrift                  | 756 us                                                 | 750 us: 1.01x faster                                                   |
| xml_etree_process       | 53.9 ms                                                | 53.7 ms: 1.00x faster                                                  |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                                   |
| django_template         | 32.6 ms                                                | 32.8 ms: 1.01x slower                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                                  |
| nbody                   | 93.1 ms                                                | 94.0 ms: 1.01x slower                                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.98 us: 1.01x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 77.3 ms: 1.01x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                 |
| unpack_sequence         | 43.1 ns                                                | 44.0 ns: 1.02x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.03x slower                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 758 ms: 1.03x slower                                                   |
| unpickle_list           | 4.91 us                                                | 5.04 us: 1.03x slower                                                  |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                                   |
| async_tree_memoization  | 627 ms                                                 | 645 ms: 1.03x slower                                                   |
| python_startup          | 8.52 ms                                                | 8.90 ms: 1.04x slower                                                  |
| generators              | 73.5 ms                                                | 77.4 ms: 1.05x slower                                                  |
| gc_traversal            | 4.02 ms                                                | 4.29 ms: 1.07x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.45 ms: 1.07x slower                                                  |
| regex_v8                | 22.0 ms                                                | 26.0 ms: 1.18x slower                                                  |
| dask                    | 360 ms                                                 | 494 ms: 1.37x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (6): async_tree_none, bench_mp_pool, sqlglot_transpile, pickle, spectral_norm, djangocms
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230127-3.12.0a4+-f23eec9/bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-f23eec9.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
