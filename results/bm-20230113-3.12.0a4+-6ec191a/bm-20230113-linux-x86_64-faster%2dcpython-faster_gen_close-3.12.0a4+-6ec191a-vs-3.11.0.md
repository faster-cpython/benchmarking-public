
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
| 2to3           | 257 ms                                                 | 250 ms: 1.03x faster                                                         |
| chameleon      | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                        |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                       |
| html5lib       | 63.2 ms                                                | 60.1 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.3 ms: 1.07x faster                                                        |
| pidigits       | 199 ms                                                 | 193 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.04x faster                                                         |
| regex_v8       | 22.3 ms                                                | 22.4 ms: 1.00x slower                                                        |
| regex_dna      | 203 ms                                                 | 215 ms: 1.06x slower                                                         |
| regex_effbot   | 3.36 ms                                                | 3.69 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.40 ms: 1.35x faster                                                        |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                         |
| json_loads           | 26.2 us                                                | 23.8 us: 1.10x faster                                                        |
| pickle_pure_python   | 304 us                                                 | 284 us: 1.07x faster                                                         |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                         |
| xml_etree_process    | 53.8 ms                                                | 53.2 ms: 1.01x faster                                                        |
| pickle_dict          | 31.4 us                                                | 31.2 us: 1.01x faster                                                        |
| unpickle_list        | 4.95 us                                                | 4.98 us: 1.01x slower                                                        |
| pickle_list          | 4.17 us                                                | 4.23 us: 1.01x slower                                                        |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (3): unpickle, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.52 ms: 1.02x slower                                                        |
| python_startup_no_site | 5.96 ms                                                | 6.09 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.0 ms: 1.11x faster                                                        |
| genshi_text     | 22.1 ms                                                | 20.5 ms: 1.08x faster                                                        |
| mako            | 9.85 ms                                                | 9.79 ms: 1.01x faster                                                        |
| django_template | 32.5 ms                                                | 32.7 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.40 ms: 1.35x faster                                                        |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                         |
| deltablue               | 3.64 ms                                                | 3.21 ms: 1.14x faster                                                        |
| genshi_xml              | 52.1 ms                                                | 47.0 ms: 1.11x faster                                                        |
| json_loads              | 26.2 us                                                | 23.8 us: 1.10x faster                                                        |
| deepcopy_memo           | 36.4 us                                                | 33.4 us: 1.09x faster                                                        |
| genshi_text             | 22.1 ms                                                | 20.5 ms: 1.08x faster                                                        |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                         |
| richards                | 46.2 ms                                                | 42.9 ms: 1.08x faster                                                        |
| float                   | 76.3 ms                                                | 71.3 ms: 1.07x faster                                                        |
| pickle_pure_python      | 304 us                                                 | 284 us: 1.07x faster                                                         |
| sympy_str               | 287 ms                                                 | 269 ms: 1.07x faster                                                         |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                         |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                         |
| json                    | 4.95 ms                                                | 4.66 ms: 1.06x faster                                                        |
| logging_silent          | 98.5 ns                                                | 92.7 ns: 1.06x faster                                                        |
| telco                   | 6.62 ms                                                | 6.25 ms: 1.06x faster                                                        |
| scimark_monte_carlo     | 68.3 ms                                                | 64.4 ms: 1.06x faster                                                        |
| logging_simple          | 6.06 us                                                | 5.74 us: 1.06x faster                                                        |
| pyflate                 | 417 ms                                                 | 395 ms: 1.06x faster                                                         |
| go                      | 143 ms                                                 | 136 ms: 1.05x faster                                                         |
| nqueens                 | 85.0 ms                                                | 80.8 ms: 1.05x faster                                                        |
| deepcopy                | 344 us                                                 | 327 us: 1.05x faster                                                         |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.05x faster                                                       |
| html5lib                | 63.2 ms                                                | 60.1 ms: 1.05x faster                                                        |
| sympy_integrate         | 20.9 ms                                                | 19.9 ms: 1.05x faster                                                        |
| scimark_fft             | 329 ms                                                 | 313 ms: 1.05x faster                                                         |
| spectral_norm           | 99.9 ms                                                | 95.3 ms: 1.05x faster                                                        |
| fannkuch                | 388 ms                                                 | 371 ms: 1.05x faster                                                         |
| regex_compile           | 136 ms                                                 | 130 ms: 1.04x faster                                                         |
| logging_format          | 6.62 us                                                | 6.34 us: 1.04x faster                                                        |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.22 ms: 1.04x faster                                                        |
| sympy_expand            | 472 ms                                                 | 453 ms: 1.04x faster                                                         |
| mdp                     | 2.62 sec                                               | 2.52 sec: 1.04x faster                                                       |
| bench_thread_pool       | 810 us                                                 | 779 us: 1.04x faster                                                         |
| hexiom                  | 6.35 ms                                                | 6.12 ms: 1.04x faster                                                        |
| unpack_sequence         | 43.4 ns                                                | 41.8 ns: 1.04x faster                                                        |
| sqlglot_optimize        | 53.0 ms                                                | 51.1 ms: 1.04x faster                                                        |
| pidigits                | 199 ms                                                 | 193 ms: 1.04x faster                                                         |
| coroutines              | 26.1 ms                                                | 25.3 ms: 1.03x faster                                                        |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                       |
| pprint_safe_repr        | 691 ms                                                 | 670 ms: 1.03x faster                                                         |
| coverage                | 101 ms                                                 | 97.5 ms: 1.03x faster                                                        |
| 2to3                    | 257 ms                                                 | 250 ms: 1.03x faster                                                         |
| dulwich_log             | 63.9 ms                                                | 62.2 ms: 1.03x faster                                                        |
| raytrace                | 290 ms                                                 | 283 ms: 1.03x faster                                                         |
| deepcopy_reduce         | 2.97 us                                                | 2.89 us: 1.03x faster                                                        |
| async_generators        | 359 ms                                                 | 352 ms: 1.02x faster                                                         |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                                       |
| chameleon               | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                        |
| meteor_contest          | 105 ms                                                 | 103 ms: 1.02x faster                                                         |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.01x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                         |
| chaos                   | 68.6 ms                                                | 67.8 ms: 1.01x faster                                                        |
| xml_etree_process       | 53.8 ms                                                | 53.2 ms: 1.01x faster                                                        |
| async_tree_none         | 529 ms                                                 | 524 ms: 1.01x faster                                                         |
| pickle_dict             | 31.4 us                                                | 31.2 us: 1.01x faster                                                        |
| mako                    | 9.85 ms                                                | 9.79 ms: 1.01x faster                                                        |
| regex_v8                | 22.3 ms                                                | 22.4 ms: 1.00x slower                                                        |
| unpickle_list           | 4.95 us                                                | 4.98 us: 1.01x slower                                                        |
| django_template         | 32.5 ms                                                | 32.7 ms: 1.01x slower                                                        |
| pickle_list             | 4.17 us                                                | 4.23 us: 1.01x slower                                                        |
| scimark_lu              | 107 ms                                                 | 109 ms: 1.01x slower                                                         |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                                        |
| python_startup          | 8.36 ms                                                | 8.52 ms: 1.02x slower                                                        |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.02x slower                                                        |
| python_startup_no_site  | 5.96 ms                                                | 6.09 ms: 1.02x slower                                                        |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                                        |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                                        |
| crypto_pyaes            | 73.9 ms                                                | 76.9 ms: 1.04x slower                                                        |
| regex_dna               | 203 ms                                                 | 215 ms: 1.06x slower                                                         |
| generators              | 72.2 ms                                                | 76.6 ms: 1.06x slower                                                        |
| regex_effbot            | 3.36 ms                                                | 3.69 ms: 1.10x slower                                                        |
| mypy                    | 669 ms                                                 | 804 ms: 1.20x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, unpickle, bench_mp_pool, async_tree_io, xml_etree_generate, thrift, nbody, xml_etree_iterparse, async_tree_memoization
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230113-3.12.0a4+-6ec191a/bm-20230113-linux-x86_64-faster%2dcpython-faster_gen_close-3.12.0a4+-6ec191a.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
