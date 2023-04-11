
# Results vs. base

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: d43bb5f
- commit date: 2023-04-10
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.01x slower                                                              |
| chameleon      | 6.47 ms                                                                | 6.52 ms: 1.01x slower                                                             |
| docutils       | 2.54 sec                                                               | 2.57 sec: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 88.8 ms                                                                | 84.4 ms: 1.05x faster                                                             |
| float          | 73.3 ms                                                                | 74.3 ms: 1.01x slower                                                             |
| pidigits       | 188 ms                                                                 | 197 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 134 ms                                                                 | 133 ms: 1.01x faster                                                              |
| regex_v8       | 22.3 ms                                                                | 22.5 ms: 1.00x slower                                                             |
| regex_dna      | 203 ms                                                                 | 208 ms: 1.02x slower                                                              |
| regex_effbot   | 3.45 ms                                                                | 3.64 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_dict          | 33.0 us                                                                | 31.9 us: 1.03x faster                                                             |
| pickle_list          | 4.46 us                                                                | 4.35 us: 1.02x faster                                                             |
| unpickle_list        | 4.99 us                                                                | 4.91 us: 1.02x faster                                                             |
| pickle               | 10.8 us                                                                | 10.7 us: 1.01x faster                                                             |
| unpickle_pure_python | 199 us                                                                 | 201 us: 1.01x slower                                                              |
| pickle_pure_python   | 286 us                                                                 | 289 us: 1.01x slower                                                              |
| xml_etree_generate   | 80.0 ms                                                                | 81.2 ms: 1.02x slower                                                             |
| json_dumps           | 9.61 ms                                                                | 9.80 ms: 1.02x slower                                                             |
| xml_etree_parse      | 148 ms                                                                 | 151 ms: 1.02x slower                                                              |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (4): unpickle, xml_etree_iterparse, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.84 ms                                                                | 8.92 ms: 1.01x slower                                                             |
| python_startup_no_site | 6.53 ms                                                                | 6.59 ms: 1.01x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 48.3 ms                                                                | 48.6 ms: 1.01x slower                                                             |
| django_template | 32.6 ms                                                                | 33.0 ms: 1.01x slower                                                             |
| mako            | 10.1 ms                                                                | 10.2 ms: 1.02x slower                                                             |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f | bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-d43bb5f |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| gc_traversal            | 4.07 ms                                                                | 3.85 ms: 1.06x faster                                                             |
| nbody                   | 88.8 ms                                                                | 84.4 ms: 1.05x faster                                                             |
| pickle_dict             | 33.0 us                                                                | 31.9 us: 1.03x faster                                                             |
| coroutines              | 22.9 ms                                                                | 22.4 ms: 1.02x faster                                                             |
| pickle_list             | 4.46 us                                                                | 4.35 us: 1.02x faster                                                             |
| unpickle_list           | 4.99 us                                                                | 4.91 us: 1.02x faster                                                             |
| thrift                  | 784 us                                                                 | 771 us: 1.02x faster                                                              |
| richards                | 43.8 ms                                                                | 43.1 ms: 1.02x faster                                                             |
| telco                   | 6.51 ms                                                                | 6.42 ms: 1.01x faster                                                             |
| chaos                   | 66.2 ms                                                                | 65.4 ms: 1.01x faster                                                             |
| go                      | 139 ms                                                                 | 137 ms: 1.01x faster                                                              |
| regex_compile           | 134 ms                                                                 | 133 ms: 1.01x faster                                                              |
| async_generators        | 415 ms                                                                 | 412 ms: 1.01x faster                                                              |
| raytrace                | 281 ms                                                                 | 279 ms: 1.01x faster                                                              |
| pickle                  | 10.8 us                                                                | 10.7 us: 1.01x faster                                                             |
| meteor_contest          | 102 ms                                                                 | 102 ms: 1.00x faster                                                              |
| aiohttp                 | 1.01 ms                                                                | 1.01 ms: 1.00x faster                                                             |
| regex_v8                | 22.3 ms                                                                | 22.5 ms: 1.00x slower                                                             |
| mypy2                   | 334 ms                                                                 | 336 ms: 1.00x slower                                                              |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.01x slower                                                              |
| unpack_sequence         | 43.6 ns                                                                | 43.8 ns: 1.01x slower                                                             |
| sqlglot_normalize       | 104 ms                                                                 | 104 ms: 1.01x slower                                                              |
| sympy_str               | 283 ms                                                                 | 284 ms: 1.01x slower                                                              |
| sympy_integrate         | 20.4 ms                                                                | 20.5 ms: 1.01x slower                                                             |
| sympy_expand            | 459 ms                                                                 | 462 ms: 1.01x slower                                                              |
| sqlglot_parse           | 1.22 ms                                                                | 1.23 ms: 1.01x slower                                                             |
| genshi_xml              | 48.3 ms                                                                | 48.6 ms: 1.01x slower                                                             |
| bench_thread_pool       | 790 us                                                                 | 796 us: 1.01x slower                                                              |
| python_startup          | 8.84 ms                                                                | 8.92 ms: 1.01x slower                                                             |
| hexiom                  | 5.99 ms                                                                | 6.04 ms: 1.01x slower                                                             |
| python_startup_no_site  | 6.53 ms                                                                | 6.59 ms: 1.01x slower                                                             |
| sympy_sum               | 165 ms                                                                 | 166 ms: 1.01x slower                                                              |
| chameleon               | 6.47 ms                                                                | 6.52 ms: 1.01x slower                                                             |
| pathlib                 | 18.2 ms                                                                | 18.3 ms: 1.01x slower                                                             |
| pycparser               | 1.15 sec                                                               | 1.16 sec: 1.01x slower                                                            |
| logging_silent          | 96.5 ns                                                                | 97.4 ns: 1.01x slower                                                             |
| django_template         | 32.6 ms                                                                | 33.0 ms: 1.01x slower                                                             |
| unpickle_pure_python    | 199 us                                                                 | 201 us: 1.01x slower                                                              |
| async_tree_io           | 1.28 sec                                                               | 1.29 sec: 1.01x slower                                                            |
| sqlglot_optimize        | 50.6 ms                                                                | 51.1 ms: 1.01x slower                                                             |
| dulwich_log             | 63.0 ms                                                                | 63.7 ms: 1.01x slower                                                             |
| pickle_pure_python      | 286 us                                                                 | 289 us: 1.01x slower                                                              |
| docutils                | 2.54 sec                                                               | 2.57 sec: 1.01x slower                                                            |
| float                   | 73.3 ms                                                                | 74.3 ms: 1.01x slower                                                             |
| deepcopy_memo           | 34.0 us                                                                | 34.5 us: 1.01x slower                                                             |
| fannkuch                | 377 ms                                                                 | 383 ms: 1.01x slower                                                              |
| scimark_lu              | 105 ms                                                                 | 107 ms: 1.01x slower                                                              |
| xml_etree_generate      | 80.0 ms                                                                | 81.2 ms: 1.02x slower                                                             |
| coverage                | 95.9 ms                                                                | 97.4 ms: 1.02x slower                                                             |
| mako                    | 10.1 ms                                                                | 10.2 ms: 1.02x slower                                                             |
| async_tree_cpu_io_mixed | 719 ms                                                                 | 732 ms: 1.02x slower                                                              |
| json_dumps              | 9.61 ms                                                                | 9.80 ms: 1.02x slower                                                             |
| regex_dna               | 203 ms                                                                 | 208 ms: 1.02x slower                                                              |
| logging_format          | 6.23 us                                                                | 6.36 us: 1.02x slower                                                             |
| json                    | 4.60 ms                                                                | 4.70 ms: 1.02x slower                                                             |
| logging_simple          | 5.63 us                                                                | 5.75 us: 1.02x slower                                                             |
| pyflate                 | 413 ms                                                                 | 422 ms: 1.02x slower                                                              |
| scimark_fft             | 301 ms                                                                 | 308 ms: 1.02x slower                                                              |
| crypto_pyaes            | 73.3 ms                                                                | 75.0 ms: 1.02x slower                                                             |
| xml_etree_parse         | 148 ms                                                                 | 151 ms: 1.02x slower                                                              |
| create_gc_cycles        | 1.47 ms                                                                | 1.50 ms: 1.03x slower                                                             |
| deepcopy                | 326 us                                                                 | 334 us: 1.03x slower                                                              |
| generators              | 29.3 ms                                                                | 30.1 ms: 1.03x slower                                                             |
| mdp                     | 2.54 sec                                                               | 2.61 sec: 1.03x slower                                                            |
| nqueens                 | 79.4 ms                                                                | 82.1 ms: 1.03x slower                                                             |
| pidigits                | 188 ms                                                                 | 197 ms: 1.05x slower                                                              |
| regex_effbot            | 3.45 ms                                                                | 3.64 ms: 1.06x slower                                                             |
| scimark_sparse_mat_mult | 4.05 ms                                                                | 4.29 ms: 1.06x slower                                                             |
| spectral_norm           | 91.2 ms                                                                | 97.8 ms: 1.07x slower                                                             |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (25): unpickle, sqlalchemy_imperative, sqlalchemy_declarative, genshi_text, pprint_safe_repr, xml_etree_iterparse, gunicorn, scimark_monte_carlo, comprehensions, asyncio_tcp, bench_mp_pool, scimark_sor, tornado_http, djangocms, json_loads, async_tree_memoization, xml_etree_process, sqlglot_transpile, deltablue, pprint_pformat, deepcopy_reduce, sqlite_synth, dask, html5lib, async_tree_none
