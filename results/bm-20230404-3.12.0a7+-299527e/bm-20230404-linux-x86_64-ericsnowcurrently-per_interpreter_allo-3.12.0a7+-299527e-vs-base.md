
# Results vs. base

- fork: ericsnowcurrently
- ref: per_interpreter_allo
- machine: linux-x86_64
- commit hash: 299527e
- commit date: 2023-04-04
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230404-linux-x86_64-python-f513d5c80672c76acbda-3.12.0a7+-f513d5c | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 253 ms: 1.01x slower                                                              |
| chameleon      | 6.38 ms                                                                | 6.46 ms: 1.01x slower                                                             |
| docutils       | 2.52 sec                                                               | 2.56 sec: 1.02x slower                                                            |
| tornado_http   | 90.7 ms                                                                | 91.6 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230404-linux-x86_64-python-f513d5c80672c76acbda-3.12.0a7+-f513d5c | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x faster                                                              |
| float          | 73.9 ms                                                                | 74.6 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230404-linux-x86_64-python-f513d5c80672c76acbda-3.12.0a7+-f513d5c | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 202 ms                                                                 | 204 ms: 1.01x slower                                                              |
| regex_compile  | 134 ms                                                                 | 135 ms: 1.01x slower                                                              |
| regex_effbot   | 3.33 ms                                                                | 3.42 ms: 1.03x slower                                                             |
| regex_v8       | 21.4 ms                                                                | 22.7 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230404-linux-x86_64-python-f513d5c80672c76acbda-3.12.0a7+-f513d5c | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle               | 10.7 us                                                                | 10.8 us: 1.01x slower                                                             |
| pickle_list          | 4.32 us                                                                | 4.36 us: 1.01x slower                                                             |
| xml_etree_parse      | 148 ms                                                                 | 150 ms: 1.01x slower                                                              |
| unpickle             | 13.7 us                                                                | 13.9 us: 1.01x slower                                                             |
| xml_etree_generate   | 80.4 ms                                                                | 81.7 ms: 1.02x slower                                                             |
| json_dumps           | 9.57 ms                                                                | 9.75 ms: 1.02x slower                                                             |
| xml_etree_process    | 55.4 ms                                                                | 56.6 ms: 1.02x slower                                                             |
| unpickle_pure_python | 200 us                                                                 | 205 us: 1.02x slower                                                              |
| pickle_pure_python   | 286 us                                                                 | 293 us: 1.02x slower                                                              |
| unpickle_list        | 4.93 us                                                                | 5.06 us: 1.03x slower                                                             |
| pickle_dict          | 31.8 us                                                                | 33.3 us: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230404-linux-x86_64-python-f513d5c80672c76acbda-3.12.0a7+-f513d5c | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.84 ms                                                                | 8.85 ms: 1.00x slower                                                             |
| python_startup_no_site | 6.52 ms                                                                | 6.53 ms: 1.00x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230404-linux-x86_64-python-f513d5c80672c76acbda-3.12.0a7+-f513d5c | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 33.0 ms                                                                | 33.3 ms: 1.01x slower                                                             |
| mako            | 10.0 ms                                                                | 10.3 ms: 1.03x slower                                                             |
| genshi_text     | 21.0 ms                                                                | 21.9 ms: 1.04x slower                                                             |
| genshi_xml      | 47.0 ms                                                                | 48.9 ms: 1.04x slower                                                             |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20230404-linux-x86_64-python-f513d5c80672c76acbda-3.12.0a7+-f513d5c | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                     | 2.71 sec                                                               | 2.56 sec: 1.06x faster                                                            |
| logging_silent          | 99.9 ns                                                                | 96.3 ns: 1.04x faster                                                             |
| scimark_lu              | 109 ms                                                                 | 107 ms: 1.02x faster                                                              |
| pprint_pformat          | 1.43 sec                                                               | 1.41 sec: 1.01x faster                                                            |
| meteor_contest          | 104 ms                                                                 | 103 ms: 1.01x faster                                                              |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x faster                                                              |
| python_startup          | 8.84 ms                                                                | 8.85 ms: 1.00x slower                                                             |
| python_startup_no_site  | 6.52 ms                                                                | 6.53 ms: 1.00x slower                                                             |
| comprehensions          | 24.0 us                                                                | 24.1 us: 1.00x slower                                                             |
| mypy2                   | 335 ms                                                                 | 336 ms: 1.00x slower                                                              |
| asyncio_tcp             | 498 ms                                                                 | 501 ms: 1.01x slower                                                              |
| crypto_pyaes            | 74.8 ms                                                                | 75.2 ms: 1.01x slower                                                             |
| pprint_safe_repr        | 688 ms                                                                 | 692 ms: 1.01x slower                                                              |
| sqlglot_normalize       | 106 ms                                                                 | 106 ms: 1.01x slower                                                              |
| deltablue               | 3.20 ms                                                                | 3.22 ms: 1.01x slower                                                             |
| 2to3                    | 251 ms                                                                 | 253 ms: 1.01x slower                                                              |
| regex_dna               | 202 ms                                                                 | 204 ms: 1.01x slower                                                              |
| aiohttp                 | 1.01 ms                                                                | 1.01 ms: 1.01x slower                                                             |
| gunicorn                | 1.08 ms                                                                | 1.09 ms: 1.01x slower                                                             |
| sqlglot_optimize        | 51.3 ms                                                                | 51.7 ms: 1.01x slower                                                             |
| regex_compile           | 134 ms                                                                 | 135 ms: 1.01x slower                                                              |
| django_template         | 33.0 ms                                                                | 33.3 ms: 1.01x slower                                                             |
| sympy_expand            | 462 ms                                                                 | 466 ms: 1.01x slower                                                              |
| sympy_str               | 283 ms                                                                 | 286 ms: 1.01x slower                                                              |
| tornado_http            | 90.7 ms                                                                | 91.6 ms: 1.01x slower                                                             |
| create_gc_cycles        | 1.47 ms                                                                | 1.48 ms: 1.01x slower                                                             |
| pickle                  | 10.7 us                                                                | 10.8 us: 1.01x slower                                                             |
| pickle_list             | 4.32 us                                                                | 4.36 us: 1.01x slower                                                             |
| float                   | 73.9 ms                                                                | 74.6 ms: 1.01x slower                                                             |
| pycparser               | 1.10 sec                                                               | 1.11 sec: 1.01x slower                                                            |
| dask                    | 509 ms                                                                 | 515 ms: 1.01x slower                                                              |
| bench_thread_pool       | 787 us                                                                 | 797 us: 1.01x slower                                                              |
| pyflate                 | 421 ms                                                                 | 426 ms: 1.01x slower                                                              |
| chameleon               | 6.38 ms                                                                | 6.46 ms: 1.01x slower                                                             |
| raytrace                | 277 ms                                                                 | 281 ms: 1.01x slower                                                              |
| async_generators        | 419 ms                                                                 | 425 ms: 1.01x slower                                                              |
| go                      | 137 ms                                                                 | 139 ms: 1.01x slower                                                              |
| sqlite_synth            | 2.60 us                                                                | 2.64 us: 1.01x slower                                                             |
| sqlalchemy_declarative  | 135 ms                                                                 | 137 ms: 1.01x slower                                                              |
| xml_etree_parse         | 148 ms                                                                 | 150 ms: 1.01x slower                                                              |
| unpickle                | 13.7 us                                                                | 13.9 us: 1.01x slower                                                             |
| docutils                | 2.52 sec                                                               | 2.56 sec: 1.02x slower                                                            |
| xml_etree_generate      | 80.4 ms                                                                | 81.7 ms: 1.02x slower                                                             |
| deepcopy_reduce         | 2.96 us                                                                | 3.00 us: 1.02x slower                                                             |
| sympy_sum               | 164 ms                                                                 | 167 ms: 1.02x slower                                                              |
| sqlglot_transpile       | 1.73 ms                                                                | 1.76 ms: 1.02x slower                                                             |
| sympy_integrate         | 20.4 ms                                                                | 20.7 ms: 1.02x slower                                                             |
| async_tree_io           | 1.28 sec                                                               | 1.30 sec: 1.02x slower                                                            |
| nqueens                 | 80.3 ms                                                                | 81.7 ms: 1.02x slower                                                             |
| deepcopy                | 327 us                                                                 | 333 us: 1.02x slower                                                              |
| scimark_sparse_mat_mult | 4.12 ms                                                                | 4.19 ms: 1.02x slower                                                             |
| sqlglot_parse           | 1.43 ms                                                                | 1.46 ms: 1.02x slower                                                             |
| json_dumps              | 9.57 ms                                                                | 9.75 ms: 1.02x slower                                                             |
| scimark_monte_carlo     | 67.7 ms                                                                | 69.0 ms: 1.02x slower                                                             |
| coroutines              | 22.9 ms                                                                | 23.3 ms: 1.02x slower                                                             |
| xml_etree_process       | 55.4 ms                                                                | 56.6 ms: 1.02x slower                                                             |
| telco                   | 6.46 ms                                                                | 6.60 ms: 1.02x slower                                                             |
| async_tree_none         | 514 ms                                                                 | 526 ms: 1.02x slower                                                              |
| unpickle_pure_python    | 200 us                                                                 | 205 us: 1.02x slower                                                              |
| coverage                | 96.1 ms                                                                | 98.3 ms: 1.02x slower                                                             |
| pickle_pure_python      | 286 us                                                                 | 293 us: 1.02x slower                                                              |
| richards                | 42.6 ms                                                                | 43.6 ms: 1.02x slower                                                             |
| hexiom                  | 6.01 ms                                                                | 6.16 ms: 1.02x slower                                                             |
| unpickle_list           | 4.93 us                                                                | 5.06 us: 1.03x slower                                                             |
| async_tree_cpu_io_mixed | 728 ms                                                                 | 747 ms: 1.03x slower                                                              |
| mako                    | 10.0 ms                                                                | 10.3 ms: 1.03x slower                                                             |
| scimark_sor             | 110 ms                                                                 | 113 ms: 1.03x slower                                                              |
| deepcopy_memo           | 34.3 us                                                                | 35.3 us: 1.03x slower                                                             |
| regex_effbot            | 3.33 ms                                                                | 3.42 ms: 1.03x slower                                                             |
| chaos                   | 66.6 ms                                                                | 68.6 ms: 1.03x slower                                                             |
| scimark_fft             | 309 ms                                                                 | 319 ms: 1.04x slower                                                              |
| genshi_text             | 21.0 ms                                                                | 21.9 ms: 1.04x slower                                                             |
| genshi_xml              | 47.0 ms                                                                | 48.9 ms: 1.04x slower                                                             |
| async_tree_memoization  | 618 ms                                                                 | 646 ms: 1.05x slower                                                              |
| pickle_dict             | 31.8 us                                                                | 33.3 us: 1.05x slower                                                             |
| fannkuch                | 368 ms                                                                 | 389 ms: 1.06x slower                                                              |
| regex_v8                | 21.4 ms                                                                | 22.7 ms: 1.06x slower                                                             |
| spectral_norm           | 92.9 ms                                                                | 99.0 ms: 1.07x slower                                                             |
| gc_traversal            | 3.66 ms                                                                | 4.31 ms: 1.18x slower                                                             |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (15): json, sqlalchemy_imperative, unpack_sequence, thrift, pathlib, logging_format, djangocms, logging_simple, json_loads, xml_etree_iterparse, nbody, bench_mp_pool, dulwich_log, generators, html5lib
