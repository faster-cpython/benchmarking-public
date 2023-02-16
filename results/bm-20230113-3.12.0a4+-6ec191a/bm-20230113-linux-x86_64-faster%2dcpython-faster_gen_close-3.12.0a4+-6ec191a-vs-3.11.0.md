
# Results vs. 3.11.0

- fork: faster-cpython
- ref: faster_gen_close
- machine: linux-x86_64
- commit hash: 6ec191a
- commit date: 2023-01-13
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                         |
| chameleon      | 6.38 ms                                                | 6.29 ms: 1.01x faster                                                        |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                       |
| html5lib       | 64.8 ms                                                | 60.1 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.3 ms: 1.08x faster                                                        |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                         |
| nbody          | 90.0 ms                                                | 95.2 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                                         |
| regex_v8       | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                        |
| regex_dna      | 203 ms                                                 | 215 ms: 1.06x slower                                                         |
| regex_effbot   | 3.46 ms                                                | 3.69 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.40 ms: 1.31x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                         |
| json_loads           | 26.1 us                                                | 23.8 us: 1.09x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 284 us: 1.08x faster                                                         |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| xml_etree_process    | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                        |
| xml_etree_generate   | 75.9 ms                                                | 76.2 ms: 1.00x slower                                                        |
| pickle_list          | 4.14 us                                                | 4.23 us: 1.02x slower                                                        |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (3): unpickle, unpickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.52 ms: 1.01x faster                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.09 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.0 ms: 1.09x faster                                                        |
| genshi_text     | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                        |
| mako            | 9.83 ms                                                | 9.79 ms: 1.00x faster                                                        |
| django_template | 32.3 ms                                                | 32.7 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 501 ms: 1.76x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.40 ms: 1.31x faster                                                        |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                         |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                                        |
| json_loads              | 26.1 us                                                | 23.8 us: 1.09x faster                                                        |
| genshi_xml              | 51.4 ms                                                | 47.0 ms: 1.09x faster                                                        |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.22 ms: 1.09x faster                                                        |
| pickle_pure_python      | 308 us                                                 | 284 us: 1.08x faster                                                         |
| sympy_str               | 291 ms                                                 | 269 ms: 1.08x faster                                                         |
| html5lib                | 64.8 ms                                                | 60.1 ms: 1.08x faster                                                        |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                         |
| float                   | 76.8 ms                                                | 71.3 ms: 1.08x faster                                                        |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                                         |
| richards                | 46.1 ms                                                | 42.9 ms: 1.08x faster                                                        |
| deepcopy_memo           | 35.8 us                                                | 33.4 us: 1.07x faster                                                        |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                         |
| unpack_sequence         | 44.5 ns                                                | 41.8 ns: 1.06x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                                       |
| pyflate                 | 419 ms                                                 | 395 ms: 1.06x faster                                                         |
| logging_silent          | 98.0 ns                                                | 92.7 ns: 1.06x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 19.9 ms: 1.06x faster                                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 64.4 ms: 1.05x faster                                                        |
| pprint_safe_repr        | 706 ms                                                 | 670 ms: 1.05x faster                                                         |
| create_gc_cycles        | 1.52 ms                                                | 1.44 ms: 1.05x faster                                                        |
| gc_traversal            | 3.82 ms                                                | 3.63 ms: 1.05x faster                                                        |
| genshi_text             | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                        |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                         |
| logging_simple          | 6.02 us                                                | 5.74 us: 1.05x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 779 us: 1.05x faster                                                         |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                                         |
| json                    | 4.87 ms                                                | 4.66 ms: 1.05x faster                                                        |
| deepcopy                | 341 us                                                 | 327 us: 1.04x faster                                                         |
| mdp                     | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                       |
| deepcopy_reduce         | 3.02 us                                                | 2.89 us: 1.04x faster                                                        |
| scimark_fft             | 325 ms                                                 | 313 ms: 1.04x faster                                                         |
| hexiom                  | 6.34 ms                                                | 6.12 ms: 1.04x faster                                                        |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                         |
| nqueens                 | 83.8 ms                                                | 80.8 ms: 1.04x faster                                                        |
| fannkuch                | 384 ms                                                 | 371 ms: 1.04x faster                                                         |
| coroutines              | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                        |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                       |
| sqlglot_optimize        | 52.7 ms                                                | 51.1 ms: 1.03x faster                                                        |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                                       |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                         |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                                         |
| spectral_norm           | 98.1 ms                                                | 95.3 ms: 1.03x faster                                                        |
| dulwich_log             | 64.0 ms                                                | 62.2 ms: 1.03x faster                                                        |
| telco                   | 6.43 ms                                                | 6.25 ms: 1.03x faster                                                        |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                         |
| logging_format          | 6.48 us                                                | 6.34 us: 1.02x faster                                                        |
| coverage                | 99.3 ms                                                | 97.5 ms: 1.02x faster                                                        |
| chameleon               | 6.38 ms                                                | 6.29 ms: 1.01x faster                                                        |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| chaos                   | 68.7 ms                                                | 67.8 ms: 1.01x faster                                                        |
| async_generators        | 356 ms                                                 | 352 ms: 1.01x faster                                                         |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                         |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| thrift                  | 760 us                                                 | 752 us: 1.01x faster                                                         |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                        |
| xml_etree_process       | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                        |
| python_startup          | 8.58 ms                                                | 8.52 ms: 1.01x faster                                                        |
| mako                    | 9.83 ms                                                | 9.79 ms: 1.00x faster                                                        |
| xml_etree_generate      | 75.9 ms                                                | 76.2 ms: 1.00x slower                                                        |
| regex_v8                | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.09 ms: 1.01x slower                                                        |
| django_template         | 32.3 ms                                                | 32.7 ms: 1.01x slower                                                        |
| crypto_pyaes            | 75.7 ms                                                | 76.9 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 748 ms: 1.02x slower                                                         |
| pickle_list             | 4.14 us                                                | 4.23 us: 1.02x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                        |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                                        |
| generators              | 73.5 ms                                                | 76.6 ms: 1.04x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                        |
| nbody                   | 90.0 ms                                                | 95.2 ms: 1.06x slower                                                        |
| regex_dna               | 203 ms                                                 | 215 ms: 1.06x slower                                                         |
| regex_effbot            | 3.46 ms                                                | 3.69 ms: 1.07x slower                                                        |
| dask                    | 365 ms                                                 | 497 ms: 1.36x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (9): djangocms, async_tree_none, unpickle, unpickle_list, pickle_dict, bench_mp_pool, async_tree_io, scimark_lu, async_tree_memoization
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230113-3.12.0a4+-6ec191a/bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a.json: mypy
