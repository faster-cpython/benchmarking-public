Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 255 ms: 1.01x faster                                                     |
| chameleon      | 6.41 ms                                                | 6.52 ms: 1.02x slower                                                    |
| docutils       | 2.60 sec                                               | 2.65 sec: 1.02x slower                                                   |
| html5lib       | 63.2 ms                                                | 60.4 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                  | 1.00x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.2 ms: 1.06x faster                                                    |
| nbody          | 95.0 ms                                                | 96.6 ms: 1.02x slower                                                    |
| pidigits       | 199 ms                                                 | 193 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                                     |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                     |
| regex_effbot   | 3.36 ms                                                | 3.58 ms: 1.07x slower                                                    |
| regex_v8       | 22.3 ms                                                | 22.4 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.43 ms: 1.34x faster                                                    |
| json_loads           | 26.2 us                                                | 23.9 us: 1.10x faster                                                    |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                    |
| pickle_dict          | 31.4 us                                                | 30.4 us: 1.03x faster                                                    |
| pickle_list          | 4.17 us                                                | 4.09 us: 1.02x faster                                                    |
| pickle_pure_python   | 304 us                                                 | 285 us: 1.07x faster                                                     |
| unpickle             | 13.3 us                                                | 13.8 us: 1.04x slower                                                    |
| unpickle_list        | 4.95 us                                                | 5.03 us: 1.01x slower                                                    |
| unpickle_pure_python | 225 us                                                 | 199 us: 1.13x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                     |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.03x slower                                                     |
| xml_etree_process    | 53.8 ms                                                | 53.2 ms: 1.01x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.55 ms: 1.02x slower                                                    |
| python_startup_no_site | 5.96 ms                                                | 6.13 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 32.0 ms: 1.01x faster                                                    |
| genshi_text     | 22.1 ms                                                | 20.6 ms: 1.07x faster                                                    |
| genshi_xml      | 52.1 ms                                                | 47.1 ms: 1.11x faster                                                    |
| mako            | 9.85 ms                                                | 9.37 ms: 1.05x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 255 ms: 1.01x faster                                                     |
| async_generators        | 359 ms                                                 | 352 ms: 1.02x faster                                                     |
| async_tree_none         | 529 ms                                                 | 541 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed | 752 ms                                                 | 769 ms: 1.02x slower                                                     |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                                   |
| async_tree_memoization  | 625 ms                                                 | 683 ms: 1.09x slower                                                     |
| chameleon               | 6.41 ms                                                | 6.52 ms: 1.02x slower                                                    |
| chaos                   | 68.6 ms                                                | 67.0 ms: 1.02x faster                                                    |
| bench_thread_pool       | 810 us                                                 | 780 us: 1.04x faster                                                     |
| coroutines              | 26.1 ms                                                | 24.9 ms: 1.05x faster                                                    |
| coverage                | 101 ms                                                 | 104 ms: 1.04x slower                                                     |
| crypto_pyaes            | 73.9 ms                                                | 75.8 ms: 1.03x slower                                                    |
| deepcopy                | 344 us                                                 | 329 us: 1.04x faster                                                     |
| deepcopy_reduce         | 2.97 us                                                | 2.91 us: 1.02x faster                                                    |
| deepcopy_memo           | 36.4 us                                                | 33.2 us: 1.10x faster                                                    |
| deltablue               | 3.64 ms                                                | 3.21 ms: 1.14x faster                                                    |
| django_template         | 32.5 ms                                                | 32.0 ms: 1.01x faster                                                    |
| docutils                | 2.60 sec                                               | 2.65 sec: 1.02x slower                                                   |
| dulwich_log             | 63.9 ms                                                | 62.2 ms: 1.03x faster                                                    |
| fannkuch                | 388 ms                                                 | 371 ms: 1.05x faster                                                     |
| float                   | 76.3 ms                                                | 72.2 ms: 1.06x faster                                                    |
| generators              | 72.2 ms                                                | 76.8 ms: 1.06x slower                                                    |
| genshi_text             | 22.1 ms                                                | 20.6 ms: 1.07x faster                                                    |
| genshi_xml              | 52.1 ms                                                | 47.1 ms: 1.11x faster                                                    |
| go                      | 143 ms                                                 | 141 ms: 1.02x faster                                                     |
| hexiom                  | 6.35 ms                                                | 6.02 ms: 1.06x faster                                                    |
| html5lib                | 63.2 ms                                                | 60.4 ms: 1.05x faster                                                    |
| json                    | 4.95 ms                                                | 5.17 ms: 1.05x slower                                                    |
| json_dumps              | 12.7 ms                                                | 9.43 ms: 1.34x faster                                                    |
| json_loads              | 26.2 us                                                | 23.9 us: 1.10x faster                                                    |
| logging_format          | 6.62 us                                                | 6.28 us: 1.05x faster                                                    |
| logging_silent          | 98.5 ns                                                | 90.9 ns: 1.08x faster                                                    |
| logging_simple          | 6.06 us                                                | 5.68 us: 1.07x faster                                                    |
| mako                    | 9.85 ms                                                | 9.37 ms: 1.05x faster                                                    |
| mdp                     | 2.62 sec                                               | 2.73 sec: 1.04x slower                                                   |
| mypy                    | 669 ms                                                 | 808 ms: 1.21x slower                                                     |
| nbody                   | 95.0 ms                                                | 96.6 ms: 1.02x slower                                                    |
| nqueens                 | 85.0 ms                                                | 78.7 ms: 1.08x faster                                                    |
| pathlib                 | 18.2 ms                                                | 17.4 ms: 1.05x faster                                                    |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                    |
| pickle_dict             | 31.4 us                                                | 30.4 us: 1.03x faster                                                    |
| pickle_list             | 4.17 us                                                | 4.09 us: 1.02x faster                                                    |
| pickle_pure_python      | 304 us                                                 | 285 us: 1.07x faster                                                     |
| pidigits                | 199 ms                                                 | 193 ms: 1.04x faster                                                     |
| pprint_safe_repr        | 691 ms                                                 | 665 ms: 1.04x faster                                                     |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.06x faster                                                   |
| pycparser               | 1.17 sec                                               | 1.16 sec: 1.02x faster                                                   |
| pyflate                 | 417 ms                                                 | 399 ms: 1.04x faster                                                     |
| python_startup          | 8.36 ms                                                | 8.55 ms: 1.02x slower                                                    |
| python_startup_no_site  | 5.96 ms                                                | 6.13 ms: 1.03x slower                                                    |
| raytrace                | 290 ms                                                 | 278 ms: 1.04x faster                                                     |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                                     |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                     |
| regex_effbot            | 3.36 ms                                                | 3.58 ms: 1.07x slower                                                    |
| regex_v8                | 22.3 ms                                                | 22.4 ms: 1.00x slower                                                    |
| richards                | 46.2 ms                                                | 45.6 ms: 1.01x faster                                                    |
| scimark_fft             | 329 ms                                                 | 312 ms: 1.05x faster                                                     |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.11x faster                                                     |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.20 ms: 1.05x faster                                                    |
| spectral_norm           | 99.9 ms                                                | 97.1 ms: 1.03x faster                                                    |
| sqlglot_parse           | 1.37 ms                                                | 1.44 ms: 1.05x slower                                                    |
| sqlglot_transpile       | 1.66 ms                                                | 1.73 ms: 1.04x slower                                                    |
| sqlglot_optimize        | 53.0 ms                                                | 50.7 ms: 1.04x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                     |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                                    |
| sympy_expand            | 472 ms                                                 | 456 ms: 1.04x faster                                                     |
| sympy_integrate         | 20.9 ms                                                | 20.5 ms: 1.02x faster                                                    |
| sympy_sum               | 166 ms                                                 | 166 ms: 1.00x slower                                                     |
| sympy_str               | 287 ms                                                 | 285 ms: 1.01x faster                                                     |
| telco                   | 6.62 ms                                                | 6.31 ms: 1.05x faster                                                    |
| thrift                  | 752 us                                                 | 763 us: 1.02x slower                                                     |
| unpack_sequence         | 43.4 ns                                                | 42.6 ns: 1.02x faster                                                    |
| unpickle                | 13.3 us                                                | 13.8 us: 1.04x slower                                                    |
| unpickle_list           | 4.95 us                                                | 5.03 us: 1.01x slower                                                    |
| unpickle_pure_python    | 225 us                                                 | 199 us: 1.13x faster                                                     |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                     |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.03x slower                                                     |
| xml_etree_process       | 53.8 ms                                                | 53.2 ms: 1.01x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (5): bench_mp_pool, meteor_contest, scimark_lu, scimark_monte_carlo, xml_etree_generate
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221222-3.12.0a3+-9e5a8e4/bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4.json: djangocms
