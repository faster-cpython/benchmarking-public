
# Results vs. 3.11.0

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: 2b105e8
- commit date: 2023-02-01
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 251 ms: 1.03x faster                                              |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                            |
| html5lib       | 63.2 ms                                                | 59.4 ms: 1.06x faster                                             |
| tornado_http   | 96.6 ms                                                | 94.3 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.8 ms: 1.05x faster                                             |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                              |
| regex_v8       | 22.3 ms                                                | 21.5 ms: 1.04x faster                                             |
| regex_dna      | 203 ms                                                 | 213 ms: 1.05x slower                                              |
| regex_effbot   | 3.36 ms                                                | 3.62 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                  | 1.00x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.40 ms: 1.35x faster                                             |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                              |
| json_loads           | 26.2 us                                                | 23.8 us: 1.10x faster                                             |
| pickle_pure_python   | 304 us                                                 | 283 us: 1.07x faster                                              |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                              |
| pickle_list          | 4.17 us                                                | 3.99 us: 1.05x faster                                             |
| pickle_dict          | 31.4 us                                                | 30.6 us: 1.03x faster                                             |
| xml_etree_process    | 53.8 ms                                                | 53.3 ms: 1.01x faster                                             |
| xml_etree_generate   | 76.2 ms                                                | 77.2 ms: 1.01x slower                                             |
| unpickle_list        | 4.95 us                                                | 5.03 us: 1.02x slower                                             |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                             |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                      |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.95 ms: 1.07x slower                                             |
| python_startup_no_site | 5.96 ms                                                | 6.48 ms: 1.09x slower                                             |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.2 ms: 1.13x faster                                             |
| genshi_text     | 22.1 ms                                                | 20.8 ms: 1.06x faster                                             |
| mako            | 9.85 ms                                                | 9.73 ms: 1.01x faster                                             |
| django_template | 32.5 ms                                                | 32.1 ms: 1.01x faster                                             |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.40 ms: 1.35x faster                                             |
| deltablue               | 3.64 ms                                                | 3.13 ms: 1.16x faster                                             |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                              |
| genshi_xml              | 52.1 ms                                                | 46.2 ms: 1.13x faster                                             |
| richards                | 46.2 ms                                                | 41.8 ms: 1.11x faster                                             |
| json_loads              | 26.2 us                                                | 23.8 us: 1.10x faster                                             |
| nqueens                 | 85.0 ms                                                | 77.3 ms: 1.10x faster                                             |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                              |
| chaos                   | 68.6 ms                                                | 63.0 ms: 1.09x faster                                             |
| logging_silent          | 98.5 ns                                                | 91.1 ns: 1.08x faster                                             |
| go                      | 143 ms                                                 | 133 ms: 1.08x faster                                              |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                              |
| pickle_pure_python      | 304 us                                                 | 283 us: 1.07x faster                                              |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                              |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                              |
| pycparser               | 1.17 sec                                               | 1.10 sec: 1.07x faster                                            |
| hexiom                  | 6.35 ms                                                | 5.94 ms: 1.07x faster                                             |
| coroutines              | 26.1 ms                                                | 24.5 ms: 1.07x faster                                             |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.13 ms: 1.07x faster                                             |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                              |
| html5lib                | 63.2 ms                                                | 59.4 ms: 1.06x faster                                             |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                              |
| json                    | 4.95 ms                                                | 4.65 ms: 1.06x faster                                             |
| genshi_text             | 22.1 ms                                                | 20.8 ms: 1.06x faster                                             |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                             |
| pyflate                 | 417 ms                                                 | 395 ms: 1.06x faster                                              |
| scimark_fft             | 329 ms                                                 | 313 ms: 1.05x faster                                              |
| float                   | 76.3 ms                                                | 72.8 ms: 1.05x faster                                             |
| aiohttp                 | 1.05 ms                                                | 999 us: 1.05x faster                                              |
| pickle_list             | 4.17 us                                                | 3.99 us: 1.05x faster                                             |
| deepcopy_memo           | 36.4 us                                                | 34.9 us: 1.05x faster                                             |
| deepcopy                | 344 us                                                 | 329 us: 1.04x faster                                              |
| logging_simple          | 6.06 us                                                | 5.81 us: 1.04x faster                                             |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.04x faster                                            |
| sympy_expand            | 472 ms                                                 | 453 ms: 1.04x faster                                              |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                             |
| telco                   | 6.62 ms                                                | 6.36 ms: 1.04x faster                                             |
| bench_thread_pool       | 810 us                                                 | 779 us: 1.04x faster                                              |
| raytrace                | 290 ms                                                 | 280 ms: 1.04x faster                                              |
| logging_format          | 6.62 us                                                | 6.37 us: 1.04x faster                                             |
| sqlglot_optimize        | 53.0 ms                                                | 51.1 ms: 1.04x faster                                             |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                            |
| scimark_monte_carlo     | 68.3 ms                                                | 65.9 ms: 1.04x faster                                             |
| coverage                | 101 ms                                                 | 97.1 ms: 1.04x faster                                             |
| regex_v8                | 22.3 ms                                                | 21.5 ms: 1.04x faster                                             |
| async_generators        | 359 ms                                                 | 348 ms: 1.03x faster                                              |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.03x faster                                             |
| deepcopy_reduce         | 2.97 us                                                | 2.88 us: 1.03x faster                                             |
| spectral_norm           | 99.9 ms                                                | 97.2 ms: 1.03x faster                                             |
| 2to3                    | 257 ms                                                 | 251 ms: 1.03x faster                                              |
| pickle_dict             | 31.4 us                                                | 30.6 us: 1.03x faster                                             |
| pprint_safe_repr        | 691 ms                                                 | 674 ms: 1.03x faster                                              |
| tornado_http            | 96.6 ms                                                | 94.3 ms: 1.02x faster                                             |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                              |
| scimark_lu              | 107 ms                                                 | 105 ms: 1.02x faster                                              |
| unpack_sequence         | 43.4 ns                                                | 42.6 ns: 1.02x faster                                             |
| mako                    | 9.85 ms                                                | 9.73 ms: 1.01x faster                                             |
| dulwich_log             | 63.9 ms                                                | 63.3 ms: 1.01x faster                                             |
| django_template         | 32.5 ms                                                | 32.1 ms: 1.01x faster                                             |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                              |
| xml_etree_process       | 53.8 ms                                                | 53.3 ms: 1.01x faster                                             |
| mdp                     | 2.62 sec                                               | 2.60 sec: 1.01x faster                                            |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                              |
| crypto_pyaes            | 73.9 ms                                                | 73.7 ms: 1.00x faster                                             |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                            |
| xml_etree_generate      | 76.2 ms                                                | 77.2 ms: 1.01x slower                                             |
| unpickle_list           | 4.95 us                                                | 5.03 us: 1.02x slower                                             |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.02x slower                                             |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                             |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                             |
| generators              | 72.2 ms                                                | 74.9 ms: 1.04x slower                                             |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                             |
| regex_dna               | 203 ms                                                 | 213 ms: 1.05x slower                                              |
| async_tree_memoization  | 625 ms                                                 | 664 ms: 1.06x slower                                              |
| python_startup          | 8.36 ms                                                | 8.95 ms: 1.07x slower                                             |
| regex_effbot            | 3.36 ms                                                | 3.62 ms: 1.08x slower                                             |
| python_startup_no_site  | 5.96 ms                                                | 6.48 ms: 1.09x slower                                             |
| mypy                    | 669 ms                                                 | 806 ms: 1.21x slower                                              |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (8): unpickle, async_tree_none, nbody, xml_etree_iterparse, thrift, bench_mp_pool, chameleon, async_tree_cpu_io_mixed
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230201-3.12.0a4+-2b105e8/bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
