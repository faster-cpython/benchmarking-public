
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: d43bb5f
- commit date: 2023-04-10
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                              |
| chameleon      | 6.47 ms                                                | 6.52 ms: 1.01x slower                                                             |
| docutils       | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                            |
| html5lib       | 64.5 ms                                                | 62.4 ms: 1.03x faster                                                             |
| tornado_http   | 96.3 ms                                                | 94.1 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 84.4 ms: 1.10x faster                                                             |
| float          | 77.2 ms                                                | 74.3 ms: 1.04x faster                                                             |
| pidigits       | 198 ms                                                 | 197 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.64 ms: 1.10x faster                                                             |
| regex_compile  | 138 ms                                                 | 133 ms: 1.04x faster                                                              |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                              |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.80 ms: 1.28x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.13x faster                                                              |
| json_loads           | 26.5 us                                                | 24.4 us: 1.09x faster                                                             |
| pickle_pure_python   | 306 us                                                 | 289 us: 1.06x faster                                                              |
| xml_etree_parse      | 158 ms                                                 | 151 ms: 1.05x faster                                                              |
| xml_etree_iterparse  | 104 ms                                                 | 99.7 ms: 1.04x faster                                                             |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.03x slower                                                             |
| xml_etree_process    | 53.9 ms                                                | 55.5 ms: 1.03x slower                                                             |
| pickle_list          | 4.11 us                                                | 4.35 us: 1.06x slower                                                             |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 81.2 ms: 1.07x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.92 ms: 1.05x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.59 ms: 1.10x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.6 ms: 1.06x faster                                                             |
| genshi_text     | 21.6 ms                                                | 21.7 ms: 1.01x slower                                                             |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                             |
| mako            | 10.1 ms                                                | 10.2 ms: 1.01x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.1 ms: 2.44x faster                                                             |
| asyncio_tcp             | 922 ms                                                 | 503 ms: 1.83x faster                                                              |
| json_dumps              | 12.6 ms                                                | 9.80 ms: 1.28x faster                                                             |
| mypy2                   | 420 ms                                                 | 336 ms: 1.25x faster                                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.23 ms: 1.14x faster                                                             |
| coroutines              | 25.5 ms                                                | 22.4 ms: 1.14x faster                                                             |
| deltablue               | 3.67 ms                                                | 3.23 ms: 1.14x faster                                                             |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.13x faster                                                              |
| sqlglot_transpile       | 1.70 ms                                                | 1.51 ms: 1.13x faster                                                             |
| nbody                   | 93.1 ms                                                | 84.4 ms: 1.10x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.64 ms: 1.10x faster                                                             |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                             |
| json_loads              | 26.5 us                                                | 24.4 us: 1.09x faster                                                             |
| deepcopy_memo           | 37.0 us                                                | 34.5 us: 1.07x faster                                                             |
| gunicorn                | 1.18 ms                                                | 1.10 ms: 1.07x faster                                                             |
| scimark_fft             | 328 ms                                                 | 308 ms: 1.07x faster                                                              |
| genshi_xml              | 51.8 ms                                                | 48.6 ms: 1.06x faster                                                             |
| raytrace                | 297 ms                                                 | 279 ms: 1.06x faster                                                              |
| richards                | 45.7 ms                                                | 43.1 ms: 1.06x faster                                                             |
| pickle_pure_python      | 306 us                                                 | 289 us: 1.06x faster                                                              |
| chaos                   | 69.2 ms                                                | 65.4 ms: 1.06x faster                                                             |
| hexiom                  | 6.37 ms                                                | 6.04 ms: 1.06x faster                                                             |
| scimark_sor             | 118 ms                                                 | 112 ms: 1.05x faster                                                              |
| json                    | 4.94 ms                                                | 4.70 ms: 1.05x faster                                                             |
| logging_format          | 6.68 us                                                | 6.36 us: 1.05x faster                                                             |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.29 ms: 1.05x faster                                                             |
| logging_simple          | 6.03 us                                                | 5.75 us: 1.05x faster                                                             |
| xml_etree_parse         | 158 ms                                                 | 151 ms: 1.05x faster                                                              |
| gc_traversal            | 4.02 ms                                                | 3.85 ms: 1.05x faster                                                             |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.04x faster                                                              |
| xml_etree_iterparse     | 104 ms                                                 | 99.7 ms: 1.04x faster                                                             |
| float                   | 77.2 ms                                                | 74.3 ms: 1.04x faster                                                             |
| sqlglot_optimize        | 53.1 ms                                                | 51.1 ms: 1.04x faster                                                             |
| regex_compile           | 138 ms                                                 | 133 ms: 1.04x faster                                                              |
| logging_silent          | 101 ns                                                 | 97.4 ns: 1.04x faster                                                             |
| html5lib                | 64.5 ms                                                | 62.4 ms: 1.03x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                              |
| comprehensions          | 22.4 us                                                | 21.8 us: 1.03x faster                                                             |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                              |
| bench_thread_pool       | 819 us                                                 | 796 us: 1.03x faster                                                              |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                                              |
| coverage                | 100 ms                                                 | 97.4 ms: 1.03x faster                                                             |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                              |
| telco                   | 6.58 ms                                                | 6.42 ms: 1.03x faster                                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 66.4 ms: 1.03x faster                                                             |
| docutils                | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                            |
| spectral_norm           | 100 ms                                                 | 97.8 ms: 1.02x faster                                                             |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                             |
| tornado_http            | 96.3 ms                                                | 94.1 ms: 1.02x faster                                                             |
| deepcopy                | 342 us                                                 | 334 us: 1.02x faster                                                              |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                                            |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                              |
| async_tree_none         | 526 ms                                                 | 516 ms: 1.02x faster                                                              |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                                              |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                            |
| pprint_safe_repr        | 701 ms                                                 | 690 ms: 1.02x faster                                                              |
| nqueens                 | 83.4 ms                                                | 82.1 ms: 1.02x faster                                                             |
| fannkuch                | 388 ms                                                 | 383 ms: 1.01x faster                                                              |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                                              |
| async_tree_cpu_io_mixed | 739 ms                                                 | 732 ms: 1.01x faster                                                              |
| pidigits                | 198 ms                                                 | 197 ms: 1.01x faster                                                              |
| mdp                     | 2.62 sec                                               | 2.61 sec: 1.00x faster                                                            |
| crypto_pyaes            | 74.7 ms                                                | 75.0 ms: 1.00x slower                                                             |
| pathlib                 | 18.2 ms                                                | 18.3 ms: 1.01x slower                                                             |
| genshi_text             | 21.6 ms                                                | 21.7 ms: 1.01x slower                                                             |
| chameleon               | 6.47 ms                                                | 6.52 ms: 1.01x slower                                                             |
| pyflate                 | 418 ms                                                 | 422 ms: 1.01x slower                                                              |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                             |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                             |
| mako                    | 10.1 ms                                                | 10.2 ms: 1.01x slower                                                             |
| unpack_sequence         | 43.1 ns                                                | 43.8 ns: 1.02x slower                                                             |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                                              |
| regex_v8                | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                             |
| thrift                  | 756 us                                                 | 771 us: 1.02x slower                                                              |
| deepcopy_reduce         | 2.94 us                                                | 3.00 us: 1.02x slower                                                             |
| pickle_dict             | 31.1 us                                                | 31.9 us: 1.03x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 55.5 ms: 1.03x slower                                                             |
| python_startup          | 8.52 ms                                                | 8.92 ms: 1.05x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.64 us: 1.05x slower                                                             |
| pickle_list             | 4.11 us                                                | 4.35 us: 1.06x slower                                                             |
| pickle                  | 10.1 us                                                | 10.7 us: 1.06x slower                                                             |
| xml_etree_generate      | 76.2 ms                                                | 81.2 ms: 1.07x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.59 ms: 1.10x slower                                                             |
| async_generators        | 368 ms                                                 | 412 ms: 1.12x slower                                                              |
| dask                    | 360 ms                                                 | 504 ms: 1.40x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                      |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_io, sympy_sum, djangocms, bench_mp_pool, unpickle_list, sqlalchemy_imperative, dulwich_log, unpickle
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
