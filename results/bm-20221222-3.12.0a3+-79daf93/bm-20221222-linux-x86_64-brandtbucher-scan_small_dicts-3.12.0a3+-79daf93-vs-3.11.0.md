
# Results vs. 3.11.0

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: 79daf93
- commit date: 2022-12-22
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 253 ms: 1.02x faster                                                     |
| chameleon      | 6.41 ms                                                | 6.54 ms: 1.02x slower                                                    |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                   |
| html5lib       | 63.2 ms                                                | 59.8 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 73.2 ms: 1.04x faster                                                    |
| pidigits       | 199 ms                                                 | 193 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                                     |
| regex_dna      | 203 ms                                                 | 204 ms: 1.00x slower                                                     |
| regex_effbot   | 3.36 ms                                                | 3.43 ms: 1.02x slower                                                    |
| regex_v8       | 22.3 ms                                                | 21.9 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.32 ms: 1.36x faster                                                    |
| json_loads           | 26.2 us                                                | 24.1 us: 1.09x faster                                                    |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                    |
| pickle_dict          | 31.4 us                                                | 31.2 us: 1.01x faster                                                    |
| pickle_list          | 4.17 us                                                | 4.11 us: 1.02x faster                                                    |
| pickle_pure_python   | 304 us                                                 | 278 us: 1.09x faster                                                     |
| unpickle_list        | 4.95 us                                                | 5.01 us: 1.01x slower                                                    |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 103 ms                                                 | 107 ms: 1.04x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 78.1 ms: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.56 ms: 1.02x slower                                                    |
| python_startup_no_site | 5.96 ms                                                | 6.12 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 22.1 ms                                                | 20.5 ms: 1.08x faster                                                    |
| genshi_xml     | 52.1 ms                                                | 47.4 ms: 1.10x faster                                                    |
| mako           | 9.85 ms                                                | 9.51 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 253 ms: 1.02x faster                                                     |
| async_generators        | 359 ms                                                 | 349 ms: 1.03x faster                                                     |
| async_tree_none         | 529 ms                                                 | 537 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed | 752 ms                                                 | 768 ms: 1.02x slower                                                     |
| async_tree_io           | 1.31 sec                                               | 1.34 sec: 1.02x slower                                                   |
| async_tree_memoization  | 625 ms                                                 | 651 ms: 1.04x slower                                                     |
| chameleon               | 6.41 ms                                                | 6.54 ms: 1.02x slower                                                    |
| chaos                   | 68.6 ms                                                | 66.4 ms: 1.03x faster                                                    |
| bench_thread_pool       | 810 us                                                 | 778 us: 1.04x faster                                                     |
| coroutines              | 26.1 ms                                                | 24.8 ms: 1.05x faster                                                    |
| coverage                | 101 ms                                                 | 97.5 ms: 1.03x faster                                                    |
| crypto_pyaes            | 73.9 ms                                                | 75.9 ms: 1.03x slower                                                    |
| deepcopy                | 344 us                                                 | 322 us: 1.07x faster                                                     |
| deepcopy_reduce         | 2.97 us                                                | 2.89 us: 1.03x faster                                                    |
| deepcopy_memo           | 36.4 us                                                | 32.9 us: 1.11x faster                                                    |
| deltablue               | 3.64 ms                                                | 3.24 ms: 1.12x faster                                                    |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                   |
| dulwich_log             | 63.9 ms                                                | 62.5 ms: 1.02x faster                                                    |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                     |
| float                   | 76.3 ms                                                | 73.2 ms: 1.04x faster                                                    |
| generators              | 72.2 ms                                                | 74.8 ms: 1.04x slower                                                    |
| genshi_text             | 22.1 ms                                                | 20.5 ms: 1.08x faster                                                    |
| genshi_xml              | 52.1 ms                                                | 47.4 ms: 1.10x faster                                                    |
| go                      | 143 ms                                                 | 132 ms: 1.09x faster                                                     |
| hexiom                  | 6.35 ms                                                | 6.10 ms: 1.04x faster                                                    |
| html5lib                | 63.2 ms                                                | 59.8 ms: 1.06x faster                                                    |
| json                    | 4.95 ms                                                | 5.03 ms: 1.02x slower                                                    |
| json_dumps              | 12.7 ms                                                | 9.32 ms: 1.36x faster                                                    |
| json_loads              | 26.2 us                                                | 24.1 us: 1.09x faster                                                    |
| logging_format          | 6.62 us                                                | 6.22 us: 1.06x faster                                                    |
| logging_silent          | 98.5 ns                                                | 91.2 ns: 1.08x faster                                                    |
| logging_simple          | 6.06 us                                                | 5.63 us: 1.08x faster                                                    |
| mako                    | 9.85 ms                                                | 9.51 ms: 1.04x faster                                                    |
| mdp                     | 2.62 sec                                               | 2.71 sec: 1.04x slower                                                   |
| meteor_contest          | 105 ms                                                 | 108 ms: 1.03x slower                                                     |
| mypy                    | 669 ms                                                 | 810 ms: 1.21x slower                                                     |
| nqueens                 | 85.0 ms                                                | 78.4 ms: 1.08x faster                                                    |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.02x faster                                                    |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                    |
| pickle_dict             | 31.4 us                                                | 31.2 us: 1.01x faster                                                    |
| pickle_list             | 4.17 us                                                | 4.11 us: 1.02x faster                                                    |
| pickle_pure_python      | 304 us                                                 | 278 us: 1.09x faster                                                     |
| pidigits                | 199 ms                                                 | 193 ms: 1.04x faster                                                     |
| pprint_safe_repr        | 691 ms                                                 | 666 ms: 1.04x faster                                                     |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.05x faster                                                   |
| pycparser               | 1.17 sec                                               | 1.10 sec: 1.06x faster                                                   |
| pyflate                 | 417 ms                                                 | 397 ms: 1.05x faster                                                     |
| python_startup          | 8.36 ms                                                | 8.56 ms: 1.02x slower                                                    |
| python_startup_no_site  | 5.96 ms                                                | 6.12 ms: 1.03x slower                                                    |
| raytrace                | 290 ms                                                 | 279 ms: 1.04x faster                                                     |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                                     |
| regex_dna               | 203 ms                                                 | 204 ms: 1.00x slower                                                     |
| regex_effbot            | 3.36 ms                                                | 3.43 ms: 1.02x slower                                                    |
| regex_v8                | 22.3 ms                                                | 21.9 ms: 1.02x faster                                                    |
| richards                | 46.2 ms                                                | 41.9 ms: 1.10x faster                                                    |
| scimark_fft             | 329 ms                                                 | 316 ms: 1.04x faster                                                     |
| scimark_monte_carlo     | 68.3 ms                                                | 65.9 ms: 1.04x faster                                                    |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                     |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.27 ms: 1.03x faster                                                    |
| spectral_norm           | 99.9 ms                                                | 95.8 ms: 1.04x faster                                                    |
| sqlglot_parse           | 1.37 ms                                                | 1.42 ms: 1.04x slower                                                    |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                                    |
| sqlglot_optimize        | 53.0 ms                                                | 50.6 ms: 1.05x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                     |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                                    |
| sympy_expand            | 472 ms                                                 | 453 ms: 1.04x faster                                                     |
| sympy_integrate         | 20.9 ms                                                | 20.5 ms: 1.02x faster                                                    |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                                     |
| sympy_str               | 287 ms                                                 | 283 ms: 1.01x faster                                                     |
| telco                   | 6.62 ms                                                | 6.24 ms: 1.06x faster                                                    |
| unpack_sequence         | 43.4 ns                                                | 42.1 ns: 1.03x faster                                                    |
| unpickle_list           | 4.95 us                                                | 5.01 us: 1.01x slower                                                    |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                     |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                     |
| xml_etree_iterparse     | 103 ms                                                 | 107 ms: 1.04x slower                                                     |
| xml_etree_generate      | 76.2 ms                                                | 78.1 ms: 1.02x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (7): bench_mp_pool, django_template, nbody, scimark_lu, thrift, unpickle, xml_etree_process
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/mdboom/Work/builds/benchmarking/results/bm-20221222-3.12.0a3+-79daf93/bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93.json: djangocms
