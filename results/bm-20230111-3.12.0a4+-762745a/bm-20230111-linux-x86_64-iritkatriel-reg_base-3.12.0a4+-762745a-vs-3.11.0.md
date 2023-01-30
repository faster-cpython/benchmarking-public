
# Results vs. 3.11.0

- fork: iritkatriel
- ref: reg_base
- machine: linux-x86_64
- commit hash: 762745a
- commit date: 2023-01-11
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 254 ms: 1.01x faster                                            |
| chameleon      | 6.41 ms                                                | 6.22 ms: 1.03x faster                                           |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                          |
| html5lib       | 63.2 ms                                                | 59.7 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.2 ms: 1.06x faster                                           |
| pidigits       | 199 ms                                                 | 193 ms: 1.04x faster                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                            |
| regex_v8       | 22.3 ms                                                | 21.9 ms: 1.02x faster                                           |
| regex_dna      | 203 ms                                                 | 217 ms: 1.07x slower                                            |
| regex_effbot   | 3.36 ms                                                | 3.76 ms: 1.12x slower                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.38 ms: 1.35x faster                                           |
| unpickle_pure_python | 225 us                                                 | 202 us: 1.12x faster                                            |
| json_loads           | 26.2 us                                                | 23.8 us: 1.10x faster                                           |
| pickle_pure_python   | 304 us                                                 | 284 us: 1.07x faster                                            |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                            |
| unpickle_list        | 4.95 us                                                | 4.85 us: 1.02x faster                                           |
| xml_etree_process    | 53.8 ms                                                | 54.2 ms: 1.01x slower                                           |
| xml_etree_generate   | 76.2 ms                                                | 77.5 ms: 1.02x slower                                           |
| pickle_dict          | 31.4 us                                                | 32.0 us: 1.02x slower                                           |
| pickle_list          | 4.17 us                                                | 4.25 us: 1.02x slower                                           |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.04x slower                                            |
| pickle               | 9.79 us                                                | 10.7 us: 1.09x slower                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                    |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 5.96 ms                                                | 6.08 ms: 1.02x slower                                           |
| python_startup         | 8.36 ms                                                | 8.54 ms: 1.02x slower                                           |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.6 ms: 1.12x faster                                           |
| genshi_text     | 22.1 ms                                                | 20.5 ms: 1.08x faster                                           |
| mako            | 9.85 ms                                                | 9.75 ms: 1.01x faster                                           |
| django_template | 32.5 ms                                                | 32.9 ms: 1.01x slower                                           |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                    |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.38 ms: 1.35x faster                                           |
| unpickle_pure_python    | 225 us                                                 | 202 us: 1.12x faster                                            |
| genshi_xml              | 52.1 ms                                                | 46.6 ms: 1.12x faster                                           |
| deltablue               | 3.64 ms                                                | 3.27 ms: 1.11x faster                                           |
| json_loads              | 26.2 us                                                | 23.8 us: 1.10x faster                                           |
| richards                | 46.2 ms                                                | 42.2 ms: 1.10x faster                                           |
| logging_simple          | 6.06 us                                                | 5.62 us: 1.08x faster                                           |
| genshi_text             | 22.1 ms                                                | 20.5 ms: 1.08x faster                                           |
| deepcopy_memo           | 36.4 us                                                | 34.0 us: 1.07x faster                                           |
| pickle_pure_python      | 304 us                                                 | 284 us: 1.07x faster                                            |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                            |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                            |
| coroutines              | 26.1 ms                                                | 24.4 ms: 1.07x faster                                           |
| pyflate                 | 417 ms                                                 | 391 ms: 1.07x faster                                            |
| scimark_monte_carlo     | 68.3 ms                                                | 64.3 ms: 1.06x faster                                           |
| json                    | 4.95 ms                                                | 4.66 ms: 1.06x faster                                           |
| telco                   | 6.62 ms                                                | 6.24 ms: 1.06x faster                                           |
| logging_format          | 6.62 us                                                | 6.24 us: 1.06x faster                                           |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                            |
| html5lib                | 63.2 ms                                                | 59.7 ms: 1.06x faster                                           |
| coverage                | 101 ms                                                 | 95.1 ms: 1.06x faster                                           |
| float                   | 76.3 ms                                                | 72.2 ms: 1.06x faster                                           |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.17 ms: 1.06x faster                                           |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.06x faster                                          |
| nqueens                 | 85.0 ms                                                | 80.6 ms: 1.06x faster                                           |
| logging_silent          | 98.5 ns                                                | 93.4 ns: 1.05x faster                                           |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                            |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                          |
| sqlglot_optimize        | 53.0 ms                                                | 50.8 ms: 1.04x faster                                           |
| hexiom                  | 6.35 ms                                                | 6.09 ms: 1.04x faster                                           |
| fannkuch                | 388 ms                                                 | 373 ms: 1.04x faster                                            |
| spectral_norm           | 99.9 ms                                                | 96.2 ms: 1.04x faster                                           |
| bench_thread_pool       | 810 us                                                 | 781 us: 1.04x faster                                            |
| pprint_safe_repr        | 691 ms                                                 | 667 ms: 1.04x faster                                            |
| pidigits                | 199 ms                                                 | 193 ms: 1.04x faster                                            |
| raytrace                | 290 ms                                                 | 281 ms: 1.03x faster                                            |
| scimark_fft             | 329 ms                                                 | 319 ms: 1.03x faster                                            |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                            |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                          |
| dulwich_log             | 63.9 ms                                                | 62.1 ms: 1.03x faster                                           |
| chameleon               | 6.41 ms                                                | 6.22 ms: 1.03x faster                                           |
| deepcopy                | 344 us                                                 | 334 us: 1.03x faster                                            |
| sympy_expand            | 472 ms                                                 | 460 ms: 1.03x faster                                            |
| sympy_integrate         | 20.9 ms                                                | 20.3 ms: 1.03x faster                                           |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                          |
| unpickle_list           | 4.95 us                                                | 4.85 us: 1.02x faster                                           |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                            |
| chaos                   | 68.6 ms                                                | 67.4 ms: 1.02x faster                                           |
| regex_v8                | 22.3 ms                                                | 21.9 ms: 1.02x faster                                           |
| sympy_str               | 287 ms                                                 | 283 ms: 1.02x faster                                            |
| 2to3                    | 257 ms                                                 | 254 ms: 1.01x faster                                            |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.01x faster                                           |
| async_generators        | 359 ms                                                 | 354 ms: 1.01x faster                                            |
| mako                    | 9.85 ms                                                | 9.75 ms: 1.01x faster                                           |
| deepcopy_reduce         | 2.97 us                                                | 2.95 us: 1.01x faster                                           |
| thrift                  | 752 us                                                 | 757 us: 1.01x slower                                            |
| xml_etree_process       | 53.8 ms                                                | 54.2 ms: 1.01x slower                                           |
| async_tree_cpu_io_mixed | 752 ms                                                 | 758 ms: 1.01x slower                                            |
| crypto_pyaes            | 73.9 ms                                                | 74.8 ms: 1.01x slower                                           |
| django_template         | 32.5 ms                                                | 32.9 ms: 1.01x slower                                           |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                           |
| xml_etree_generate      | 76.2 ms                                                | 77.5 ms: 1.02x slower                                           |
| pickle_dict             | 31.4 us                                                | 32.0 us: 1.02x slower                                           |
| pickle_list             | 4.17 us                                                | 4.25 us: 1.02x slower                                           |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                          |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                           |
| python_startup_no_site  | 5.96 ms                                                | 6.08 ms: 1.02x slower                                           |
| scimark_lu              | 107 ms                                                 | 110 ms: 1.02x slower                                            |
| python_startup          | 8.36 ms                                                | 8.54 ms: 1.02x slower                                           |
| meteor_contest          | 105 ms                                                 | 108 ms: 1.03x slower                                            |
| sqlite_synth            | 2.49 us                                                | 2.57 us: 1.03x slower                                           |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.04x slower                                            |
| generators              | 72.2 ms                                                | 75.4 ms: 1.04x slower                                           |
| regex_dna               | 203 ms                                                 | 217 ms: 1.07x slower                                            |
| async_tree_memoization  | 625 ms                                                 | 670 ms: 1.07x slower                                            |
| pickle                  | 9.79 us                                                | 10.7 us: 1.09x slower                                           |
| regex_effbot            | 3.36 ms                                                | 3.76 ms: 1.12x slower                                           |
| mypy                    | 669 ms                                                 | 809 ms: 1.21x slower                                            |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                    |

Benchmark hidden because not significant (5): nbody, unpack_sequence, bench_mp_pool, async_tree_none, unpickle
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230111-3.12.0a4+-762745a/bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
