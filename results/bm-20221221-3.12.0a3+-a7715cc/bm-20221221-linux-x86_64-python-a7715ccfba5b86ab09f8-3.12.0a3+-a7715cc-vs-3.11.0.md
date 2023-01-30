
# Results vs. 3.11.0

- fork: python
- ref: a7715ccfba5b86ab09f8
- machine: linux-x86_64
- commit hash: a7715cc
- commit date: 2022-12-21
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 253 ms: 1.02x faster                                                   |
| chameleon      | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                  |
| docutils       | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                 |
| html5lib       | 63.2 ms                                                | 59.5 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.8 ms: 1.06x faster                                                  |
| nbody          | 95.0 ms                                                | 93.1 ms: 1.02x faster                                                  |
| pidigits       | 199 ms                                                 | 197 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.04x faster                                                   |
| regex_v8       | 22.3 ms                                                | 21.7 ms: 1.03x faster                                                  |
| regex_dna      | 203 ms                                                 | 203 ms: 1.00x slower                                                   |
| regex_effbot   | 3.36 ms                                                | 3.45 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.43 ms: 1.34x faster                                                  |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.15x faster                                                   |
| json_loads           | 26.2 us                                                | 23.6 us: 1.11x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                   |
| pickle_pure_python   | 304 us                                                 | 283 us: 1.07x faster                                                   |
| pickle_list          | 4.17 us                                                | 3.98 us: 1.05x faster                                                  |
| pickle_dict          | 31.4 us                                                | 30.6 us: 1.03x faster                                                  |
| unpickle_list        | 4.95 us                                                | 4.93 us: 1.01x faster                                                  |
| xml_etree_generate   | 76.2 ms                                                | 76.5 ms: 1.00x slower                                                  |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.03x slower                                                   |
| pickle               | 9.79 us                                                | 10.4 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.43 ms: 1.01x slower                                                  |
| python_startup_no_site | 5.96 ms                                                | 6.09 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 47.6 ms: 1.09x faster                                                  |
| genshi_text    | 22.1 ms                                                | 20.4 ms: 1.08x faster                                                  |
| mako           | 9.85 ms                                                | 9.47 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.43 ms: 1.34x faster                                                  |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.15x faster                                                   |
| deltablue               | 3.64 ms                                                | 3.20 ms: 1.14x faster                                                  |
| richards                | 46.2 ms                                                | 41.4 ms: 1.12x faster                                                  |
| json_loads              | 26.2 us                                                | 23.6 us: 1.11x faster                                                  |
| genshi_xml              | 52.1 ms                                                | 47.6 ms: 1.09x faster                                                  |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.09x faster                                                   |
| logging_silent          | 98.5 ns                                                | 90.4 ns: 1.09x faster                                                  |
| nqueens                 | 85.0 ms                                                | 78.5 ms: 1.08x faster                                                  |
| genshi_text             | 22.1 ms                                                | 20.4 ms: 1.08x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                   |
| pickle_pure_python      | 304 us                                                 | 283 us: 1.07x faster                                                   |
| deepcopy_memo           | 36.4 us                                                | 33.9 us: 1.07x faster                                                  |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.10 ms: 1.07x faster                                                  |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                                   |
| json                    | 4.95 ms                                                | 4.63 ms: 1.07x faster                                                  |
| pycparser               | 1.17 sec                                               | 1.10 sec: 1.07x faster                                                 |
| logging_simple          | 6.06 us                                                | 5.68 us: 1.07x faster                                                  |
| scimark_fft             | 329 ms                                                 | 309 ms: 1.07x faster                                                   |
| scimark_monte_carlo     | 68.3 ms                                                | 64.2 ms: 1.06x faster                                                  |
| logging_format          | 6.62 us                                                | 6.22 us: 1.06x faster                                                  |
| float                   | 76.3 ms                                                | 71.8 ms: 1.06x faster                                                  |
| coroutines              | 26.1 ms                                                | 24.5 ms: 1.06x faster                                                  |
| pprint_pformat          | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                 |
| html5lib                | 63.2 ms                                                | 59.5 ms: 1.06x faster                                                  |
| sqlglot_optimize        | 53.0 ms                                                | 50.1 ms: 1.06x faster                                                  |
| spectral_norm           | 99.9 ms                                                | 94.8 ms: 1.05x faster                                                  |
| hexiom                  | 6.35 ms                                                | 6.02 ms: 1.05x faster                                                  |
| telco                   | 6.62 ms                                                | 6.29 ms: 1.05x faster                                                  |
| pyflate                 | 417 ms                                                 | 396 ms: 1.05x faster                                                   |
| unpack_sequence         | 43.4 ns                                                | 41.3 ns: 1.05x faster                                                  |
| deepcopy                | 344 us                                                 | 328 us: 1.05x faster                                                   |
| pickle_list             | 4.17 us                                                | 3.98 us: 1.05x faster                                                  |
| sympy_expand            | 472 ms                                                 | 451 ms: 1.05x faster                                                   |
| docutils                | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                 |
| pprint_safe_repr        | 691 ms                                                 | 661 ms: 1.04x faster                                                   |
| regex_compile           | 136 ms                                                 | 130 ms: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| go                      | 143 ms                                                 | 138 ms: 1.04x faster                                                   |
| mako                    | 9.85 ms                                                | 9.47 ms: 1.04x faster                                                  |
| raytrace                | 290 ms                                                 | 280 ms: 1.04x faster                                                   |
| bench_thread_pool       | 810 us                                                 | 783 us: 1.03x faster                                                   |
| mdp                     | 2.62 sec                                               | 2.54 sec: 1.03x faster                                                 |
| sympy_integrate         | 20.9 ms                                                | 20.2 ms: 1.03x faster                                                  |
| regex_v8                | 22.3 ms                                                | 21.7 ms: 1.03x faster                                                  |
| pickle_dict             | 31.4 us                                                | 30.6 us: 1.03x faster                                                  |
| sympy_str               | 287 ms                                                 | 280 ms: 1.03x faster                                                   |
| deepcopy_reduce         | 2.97 us                                                | 2.90 us: 1.02x faster                                                  |
| sympy_sum               | 166 ms                                                 | 162 ms: 1.02x faster                                                   |
| dulwich_log             | 63.9 ms                                                | 62.6 ms: 1.02x faster                                                  |
| nbody                   | 95.0 ms                                                | 93.1 ms: 1.02x faster                                                  |
| 2to3                    | 257 ms                                                 | 253 ms: 1.02x faster                                                   |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                  |
| thrift                  | 752 us                                                 | 741 us: 1.01x faster                                                   |
| pidigits                | 199 ms                                                 | 197 ms: 1.01x faster                                                   |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                                   |
| async_generators        | 359 ms                                                 | 356 ms: 1.01x faster                                                   |
| chameleon               | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                  |
| unpickle_list           | 4.95 us                                                | 4.93 us: 1.01x faster                                                  |
| regex_dna               | 203 ms                                                 | 203 ms: 1.00x slower                                                   |
| xml_etree_generate      | 76.2 ms                                                | 76.5 ms: 1.00x slower                                                  |
| crypto_pyaes            | 73.9 ms                                                | 74.4 ms: 1.01x slower                                                  |
| python_startup          | 8.36 ms                                                | 8.43 ms: 1.01x slower                                                  |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                 |
| async_tree_none         | 529 ms                                                 | 535 ms: 1.01x slower                                                   |
| sqlglot_transpile       | 1.66 ms                                                | 1.68 ms: 1.01x slower                                                  |
| coverage                | 101 ms                                                 | 102 ms: 1.01x slower                                                   |
| sqlglot_parse           | 1.37 ms                                                | 1.39 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 752 ms                                                 | 765 ms: 1.02x slower                                                   |
| python_startup_no_site  | 5.96 ms                                                | 6.09 ms: 1.02x slower                                                  |
| regex_effbot            | 3.36 ms                                                | 3.45 ms: 1.03x slower                                                  |
| async_tree_memoization  | 625 ms                                                 | 644 ms: 1.03x slower                                                   |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.03x slower                                                   |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.03x slower                                                  |
| pickle                  | 9.79 us                                                | 10.4 us: 1.06x slower                                                  |
| generators              | 72.2 ms                                                | 77.4 ms: 1.07x slower                                                  |
| mypy                    | 669 ms                                                 | 803 ms: 1.20x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (6): scimark_lu, unpickle, xml_etree_process, bench_mp_pool, django_template, chaos
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
