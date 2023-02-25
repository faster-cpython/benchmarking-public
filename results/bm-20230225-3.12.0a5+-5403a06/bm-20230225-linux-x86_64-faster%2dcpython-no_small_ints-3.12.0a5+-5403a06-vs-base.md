
# Results vs. base

- fork: faster-cpython
- ref: no_small_ints
- machine: linux-x86_64
- commit hash: 5403a06
- commit date: 2023-02-25
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                 | 249 ms: 1.00x slower                                                      |
| chameleon      | 6.34 ms                                                                | 6.46 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 193 ms                                                                 | 190 ms: 1.02x faster                                                      |
| float          | 73.7 ms                                                                | 74.9 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                 | 206 ms: 1.02x faster                                                      |
| regex_v8       | 22.3 ms                                                                | 21.9 ms: 1.02x faster                                                     |
| regex_compile  | 132 ms                                                                 | 135 ms: 1.02x slower                                                      |
| regex_effbot   | 3.38 ms                                                                | 3.69 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_list      | 5.09 us                                                                | 4.97 us: 1.02x faster                                                     |
| pickle             | 10.2 us                                                                | 10.1 us: 1.01x faster                                                     |
| json_loads         | 23.7 us                                                                | 23.5 us: 1.01x faster                                                     |
| xml_etree_process  | 55.4 ms                                                                | 55.0 ms: 1.01x faster                                                     |
| json_dumps         | 9.33 ms                                                                | 9.28 ms: 1.00x faster                                                     |
| pickle_dict        | 31.4 us                                                                | 31.5 us: 1.00x slower                                                     |
| xml_etree_generate | 80.2 ms                                                                | 80.6 ms: 1.01x slower                                                     |
| pickle_pure_python | 283 us                                                                 | 286 us: 1.01x slower                                                      |
| pickle_list        | 4.16 us                                                                | 4.25 us: 1.02x slower                                                     |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_parse, unpickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.53 ms                                                                | 6.57 ms: 1.01x slower                                                     |
| python_startup         | 9.00 ms                                                                | 9.07 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 10.1 ms                                                                | 10.0 ms: 1.01x faster                                                     |
| django_template | 33.1 ms                                                                | 33.3 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230224-linux-x86_64-python-1fa38906f0b228e6b0a6-3.12.0a5+-1fa3890 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| scimark_sparse_mat_mult | 4.70 ms                                                                | 4.52 ms: 1.04x faster                                                     |
| pathlib                 | 18.3 ms                                                                | 17.7 ms: 1.04x faster                                                     |
| regex_dna               | 210 ms                                                                 | 206 ms: 1.02x faster                                                      |
| unpickle_list           | 5.09 us                                                                | 4.97 us: 1.02x faster                                                     |
| regex_v8                | 22.3 ms                                                                | 21.9 ms: 1.02x faster                                                     |
| pidigits                | 193 ms                                                                 | 190 ms: 1.02x faster                                                      |
| richards                | 42.0 ms                                                                | 41.4 ms: 1.01x faster                                                     |
| logging_silent          | 94.7 ns                                                                | 93.4 ns: 1.01x faster                                                     |
| dulwich_log             | 63.7 ms                                                                | 62.8 ms: 1.01x faster                                                     |
| deepcopy_reduce         | 2.98 us                                                                | 2.95 us: 1.01x faster                                                     |
| sqlglot_normalize       | 105 ms                                                                 | 104 ms: 1.01x faster                                                      |
| pickle                  | 10.2 us                                                                | 10.1 us: 1.01x faster                                                     |
| json_loads              | 23.7 us                                                                | 23.5 us: 1.01x faster                                                     |
| sympy_expand            | 457 ms                                                                 | 453 ms: 1.01x faster                                                      |
| sqlite_synth            | 2.65 us                                                                | 2.62 us: 1.01x faster                                                     |
| sympy_str               | 284 ms                                                                 | 282 ms: 1.01x faster                                                      |
| xml_etree_process       | 55.4 ms                                                                | 55.0 ms: 1.01x faster                                                     |
| mako                    | 10.1 ms                                                                | 10.0 ms: 1.01x faster                                                     |
| mypy2                   | 333 ms                                                                 | 331 ms: 1.01x faster                                                      |
| sympy_sum               | 167 ms                                                                 | 166 ms: 1.01x faster                                                      |
| sqlglot_optimize        | 50.8 ms                                                                | 50.5 ms: 1.01x faster                                                     |
| json_dumps              | 9.33 ms                                                                | 9.28 ms: 1.00x faster                                                     |
| asyncio_tcp             | 502 ms                                                                 | 500 ms: 1.00x faster                                                      |
| create_gc_cycles        | 1.50 ms                                                                | 1.50 ms: 1.00x faster                                                     |
| pickle_dict             | 31.4 us                                                                | 31.5 us: 1.00x slower                                                     |
| 2to3                    | 249 ms                                                                 | 249 ms: 1.00x slower                                                      |
| pprint_pformat          | 1.38 sec                                                               | 1.39 sec: 1.01x slower                                                    |
| sqlglot_transpile       | 1.72 ms                                                                | 1.73 ms: 1.01x slower                                                     |
| xml_etree_generate      | 80.2 ms                                                                | 80.6 ms: 1.01x slower                                                     |
| coverage                | 99.0 ms                                                                | 99.6 ms: 1.01x slower                                                     |
| django_template         | 33.1 ms                                                                | 33.3 ms: 1.01x slower                                                     |
| python_startup_no_site  | 6.53 ms                                                                | 6.57 ms: 1.01x slower                                                     |
| python_startup          | 9.00 ms                                                                | 9.07 ms: 1.01x slower                                                     |
| unpack_sequence         | 44.2 ns                                                                | 44.7 ns: 1.01x slower                                                     |
| pycparser               | 1.10 sec                                                               | 1.11 sec: 1.01x slower                                                    |
| logging_format          | 6.31 us                                                                | 6.37 us: 1.01x slower                                                     |
| sqlglot_parse           | 1.43 ms                                                                | 1.44 ms: 1.01x slower                                                     |
| async_generators        | 417 ms                                                                 | 422 ms: 1.01x slower                                                      |
| pickle_pure_python      | 283 us                                                                 | 286 us: 1.01x slower                                                      |
| deltablue               | 3.14 ms                                                                | 3.19 ms: 1.02x slower                                                     |
| float                   | 73.7 ms                                                                | 74.9 ms: 1.02x slower                                                     |
| logging_simple          | 5.71 us                                                                | 5.81 us: 1.02x slower                                                     |
| chameleon               | 6.34 ms                                                                | 6.46 ms: 1.02x slower                                                     |
| meteor_contest          | 102 ms                                                                 | 104 ms: 1.02x slower                                                      |
| regex_compile           | 132 ms                                                                 | 135 ms: 1.02x slower                                                      |
| pickle_list             | 4.16 us                                                                | 4.25 us: 1.02x slower                                                     |
| scimark_monte_carlo     | 67.0 ms                                                                | 68.7 ms: 1.02x slower                                                     |
| nqueens                 | 80.9 ms                                                                | 82.9 ms: 1.02x slower                                                     |
| hexiom                  | 6.11 ms                                                                | 6.27 ms: 1.03x slower                                                     |
| coroutines              | 23.6 ms                                                                | 24.3 ms: 1.03x slower                                                     |
| generators              | 29.7 ms                                                                | 30.8 ms: 1.04x slower                                                     |
| go                      | 134 ms                                                                 | 139 ms: 1.04x slower                                                      |
| mdp                     | 2.53 sec                                                               | 2.65 sec: 1.04x slower                                                    |
| crypto_pyaes            | 74.9 ms                                                                | 78.4 ms: 1.05x slower                                                     |
| pyflate                 | 414 ms                                                                 | 435 ms: 1.05x slower                                                      |
| scimark_sor             | 106 ms                                                                 | 111 ms: 1.05x slower                                                      |
| chaos                   | 67.0 ms                                                                | 70.8 ms: 1.06x slower                                                     |
| fannkuch                | 359 ms                                                                 | 389 ms: 1.08x slower                                                      |
| regex_effbot            | 3.38 ms                                                                | 3.69 ms: 1.09x slower                                                     |
| spectral_norm           | 94.5 ms                                                                | 105 ms: 1.11x slower                                                      |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (33): sqlalchemy_imperative, djangocms, async_tree_io, sqlalchemy_declarative, nbody, tornado_http, scimark_fft, thrift, deepcopy_memo, deepcopy, docutils, aiohttp, html5lib, xml_etree_iterparse, bench_thread_pool, async_tree_none, sympy_integrate, genshi_xml, raytrace, bench_mp_pool, gc_traversal, async_tree_cpu_io_mixed, xml_etree_parse, gunicorn, pprint_safe_repr, unpickle, genshi_text, scimark_lu, unpickle_pure_python, telco, dask, json, async_tree_memoization
