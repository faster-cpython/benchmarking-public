Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                   |
| chameleon      | 6.41 ms                                                | 6.35 ms: 1.01x faster                                  |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                 |
| html5lib       | 63.2 ms                                                | 59.2 ms: 1.07x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.9 ms: 1.06x faster                                  |
| nbody          | 95.0 ms                                                | 94.4 ms: 1.01x faster                                  |
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                   |
| regex_dna      | 203 ms                                                 | 210 ms: 1.04x slower                                   |
| regex_effbot   | 3.36 ms                                                | 3.47 ms: 1.03x slower                                  |
| regex_v8       | 22.3 ms                                                | 22.4 ms: 1.00x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.49 ms: 1.33x faster                                  |
| json_loads           | 26.2 us                                                | 23.9 us: 1.10x faster                                  |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                  |
| pickle_dict          | 31.4 us                                                | 30.9 us: 1.02x faster                                  |
| pickle_pure_python   | 304 us                                                 | 282 us: 1.08x faster                                   |
| unpickle             | 13.3 us                                                | 14.1 us: 1.06x slower                                  |
| unpickle_list        | 4.95 us                                                | 5.01 us: 1.01x slower                                  |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.15x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 146 ms: 1.08x faster                                   |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.01x faster                                   |
| xml_etree_generate   | 76.2 ms                                                | 77.2 ms: 1.01x slower                                  |
| xml_etree_process    | 53.8 ms                                                | 54.2 ms: 1.01x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.41 ms: 1.01x slower                                  |
| python_startup_no_site | 5.96 ms                                                | 6.07 ms: 1.02x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text    | 22.1 ms                                                | 20.0 ms: 1.10x faster                                  |
| genshi_xml     | 52.1 ms                                                | 46.3 ms: 1.12x faster                                  |
| mako           | 9.85 ms                                                | 9.46 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                   |
| async_generators        | 359 ms                                                 | 356 ms: 1.01x faster                                   |
| async_tree_cpu_io_mixed | 752 ms                                                 | 763 ms: 1.02x slower                                   |
| async_tree_io           | 1.31 sec                                               | 1.34 sec: 1.02x slower                                 |
| async_tree_memoization  | 625 ms                                                 | 656 ms: 1.05x slower                                   |
| chameleon               | 6.41 ms                                                | 6.35 ms: 1.01x faster                                  |
| chaos                   | 68.6 ms                                                | 66.6 ms: 1.03x faster                                  |
| bench_thread_pool       | 810 us                                                 | 775 us: 1.04x faster                                   |
| coroutines              | 26.1 ms                                                | 25.8 ms: 1.01x faster                                  |
| crypto_pyaes            | 73.9 ms                                                | 74.8 ms: 1.01x slower                                  |
| deepcopy                | 344 us                                                 | 329 us: 1.05x faster                                   |
| deepcopy_reduce         | 2.97 us                                                | 2.88 us: 1.03x faster                                  |
| deepcopy_memo           | 36.4 us                                                | 33.7 us: 1.08x faster                                  |
| deltablue               | 3.64 ms                                                | 3.21 ms: 1.14x faster                                  |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                 |
| dulwich_log             | 63.9 ms                                                | 61.6 ms: 1.04x faster                                  |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                   |
| float                   | 76.3 ms                                                | 71.9 ms: 1.06x faster                                  |
| generators              | 72.2 ms                                                | 78.3 ms: 1.09x slower                                  |
| genshi_text             | 22.1 ms                                                | 20.0 ms: 1.10x faster                                  |
| genshi_xml              | 52.1 ms                                                | 46.3 ms: 1.12x faster                                  |
| go                      | 143 ms                                                 | 131 ms: 1.10x faster                                   |
| hexiom                  | 6.35 ms                                                | 6.09 ms: 1.04x faster                                  |
| html5lib                | 63.2 ms                                                | 59.2 ms: 1.07x faster                                  |
| json                    | 4.95 ms                                                | 4.59 ms: 1.08x faster                                  |
| json_dumps              | 12.7 ms                                                | 9.49 ms: 1.33x faster                                  |
| json_loads              | 26.2 us                                                | 23.9 us: 1.10x faster                                  |
| logging_format          | 6.62 us                                                | 6.33 us: 1.05x faster                                  |
| logging_silent          | 98.5 ns                                                | 93.0 ns: 1.06x faster                                  |
| logging_simple          | 6.06 us                                                | 5.69 us: 1.07x faster                                  |
| mako                    | 9.85 ms                                                | 9.46 ms: 1.04x faster                                  |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.05x faster                                 |
| mypy                    | 669 ms                                                 | 802 ms: 1.20x slower                                   |
| nbody                   | 95.0 ms                                                | 94.4 ms: 1.01x faster                                  |
| nqueens                 | 85.0 ms                                                | 78.6 ms: 1.08x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.5 ms: 1.04x faster                                  |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                  |
| pickle_dict             | 31.4 us                                                | 30.9 us: 1.02x faster                                  |
| pickle_pure_python      | 304 us                                                 | 282 us: 1.08x faster                                   |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                   |
| pprint_safe_repr        | 691 ms                                                 | 675 ms: 1.02x faster                                   |
| pprint_pformat          | 1.44 sec                                               | 1.39 sec: 1.04x faster                                 |
| pycparser               | 1.17 sec                                               | 1.09 sec: 1.08x faster                                 |
| pyflate                 | 417 ms                                                 | 395 ms: 1.06x faster                                   |
| python_startup          | 8.36 ms                                                | 8.41 ms: 1.01x slower                                  |
| python_startup_no_site  | 5.96 ms                                                | 6.07 ms: 1.02x slower                                  |
| raytrace                | 290 ms                                                 | 282 ms: 1.03x faster                                   |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                   |
| regex_dna               | 203 ms                                                 | 210 ms: 1.04x slower                                   |
| regex_effbot            | 3.36 ms                                                | 3.47 ms: 1.03x slower                                  |
| regex_v8                | 22.3 ms                                                | 22.4 ms: 1.00x slower                                  |
| richards                | 46.2 ms                                                | 41.7 ms: 1.11x faster                                  |
| scimark_fft             | 329 ms                                                 | 310 ms: 1.06x faster                                   |
| scimark_lu              | 107 ms                                                 | 105 ms: 1.02x faster                                   |
| scimark_monte_carlo     | 68.3 ms                                                | 65.5 ms: 1.04x faster                                  |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                   |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.10 ms: 1.07x faster                                  |
| spectral_norm           | 99.9 ms                                                | 93.6 ms: 1.07x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.38 ms: 1.01x slower                                  |
| sqlglot_transpile       | 1.66 ms                                                | 1.67 ms: 1.01x slower                                  |
| sqlglot_optimize        | 53.0 ms                                                | 49.9 ms: 1.06x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                   |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.03x slower                                  |
| sympy_expand            | 472 ms                                                 | 447 ms: 1.06x faster                                   |
| sympy_integrate         | 20.9 ms                                                | 20.1 ms: 1.04x faster                                  |
| sympy_sum               | 166 ms                                                 | 161 ms: 1.03x faster                                   |
| sympy_str               | 287 ms                                                 | 277 ms: 1.04x faster                                   |
| telco                   | 6.62 ms                                                | 6.23 ms: 1.06x faster                                  |
| thrift                  | 752 us                                                 | 744 us: 1.01x faster                                   |
| unpickle                | 13.3 us                                                | 14.1 us: 1.06x slower                                  |
| unpickle_list           | 4.95 us                                                | 5.01 us: 1.01x slower                                  |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.15x faster                                   |
| xml_etree_parse         | 158 ms                                                 | 146 ms: 1.08x faster                                   |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.01x faster                                   |
| xml_etree_generate      | 76.2 ms                                                | 77.2 ms: 1.01x slower                                  |
| xml_etree_process       | 53.8 ms                                                | 54.2 ms: 1.01x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (7): async_tree_none, bench_mp_pool, coverage, django_template, meteor_contest, pickle_list, unpack_sequence
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
