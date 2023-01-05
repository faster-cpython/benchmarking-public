Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                    |
| chameleon      | 8.86 ms                                                | 6.17 ms: 1.44x faster                                                   |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                  |
| html5lib       | 85.8 ms                                                | 60.1 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.36x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 108 ms                                                 | 71.7 ms: 1.50x faster                                                   |
| nbody          | 136 ms                                                 | 92.8 ms: 1.47x faster                                                   |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.30x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 131 ms: 1.32x faster                                                    |
| regex_dna      | 214 ms                                                 | 211 ms: 1.01x faster                                                    |
| regex_effbot   | 3.21 ms                                                | 3.58 ms: 1.12x slower                                                   |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.42 ms: 1.43x faster                                                   |
| json_loads           | 28.9 us                                                | 24.0 us: 1.20x faster                                                   |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                   |
| pickle_dict          | 28.3 us                                                | 30.4 us: 1.07x slower                                                   |
| pickle_list          | 4.50 us                                                | 4.11 us: 1.10x faster                                                   |
| pickle_pure_python   | 453 us                                                 | 282 us: 1.61x faster                                                    |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                                   |
| unpickle_list        | 4.99 us                                                | 4.94 us: 1.01x faster                                                   |
| unpickle_pure_python | 297 us                                                 | 196 us: 1.51x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 110 ms                                                 | 104 ms: 1.06x faster                                                    |
| xml_etree_generate   | 93.3 ms                                                | 75.7 ms: 1.23x faster                                                   |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.48 ms: 1.64x faster                                                   |
| python_startup_no_site | 5.76 ms                                                | 6.08 ms: 1.05x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.3 ms: 1.43x faster                                                   |
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                   |
| genshi_xml      | 63.6 ms                                                | 46.3 ms: 1.37x faster                                                   |
| mako            | 14.3 ms                                                | 9.83 ms: 1.45x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                    |
| async_generators        | 428 ms                                                 | 355 ms: 1.21x faster                                                    |
| async_tree_none         | 713 ms                                                 | 524 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed | 949 ms                                                 | 750 ms: 1.26x faster                                                    |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 623 ms: 1.37x faster                                                    |
| chameleon               | 8.86 ms                                                | 6.17 ms: 1.44x faster                                                   |
| chaos                   | 104 ms                                                 | 67.9 ms: 1.53x faster                                                   |
| bench_thread_pool       | 943 us                                                 | 774 us: 1.22x faster                                                    |
| coroutines              | 31.7 ms                                                | 25.0 ms: 1.27x faster                                                   |
| coverage                | 75.3 ms                                                | 98.7 ms: 1.31x slower                                                   |
| crypto_pyaes            | 118 ms                                                 | 73.5 ms: 1.60x faster                                                   |
| deepcopy                | 429 us                                                 | 330 us: 1.30x faster                                                    |
| deepcopy_reduce         | 3.75 us                                                | 2.90 us: 1.29x faster                                                   |
| deepcopy_memo           | 50.0 us                                                | 33.7 us: 1.48x faster                                                   |
| deltablue               | 7.39 ms                                                | 3.34 ms: 2.21x faster                                                   |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.43x faster                                                   |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                  |
| dulwich_log             | 75.5 ms                                                | 62.0 ms: 1.22x faster                                                   |
| fannkuch                | 477 ms                                                 | 368 ms: 1.30x faster                                                    |
| float                   | 108 ms                                                 | 71.7 ms: 1.50x faster                                                   |
| generators              | 75.8 ms                                                | 77.1 ms: 1.02x slower                                                   |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                   |
| genshi_xml              | 63.6 ms                                                | 46.3 ms: 1.37x faster                                                   |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                    |
| hexiom                  | 9.42 ms                                                | 6.09 ms: 1.55x faster                                                   |
| html5lib                | 85.8 ms                                                | 60.1 ms: 1.43x faster                                                   |
| json                    | 5.35 ms                                                | 4.73 ms: 1.13x faster                                                   |
| json_dumps              | 13.5 ms                                                | 9.42 ms: 1.43x faster                                                   |
| json_loads              | 28.9 us                                                | 24.0 us: 1.20x faster                                                   |
| logging_format          | 8.92 us                                                | 6.35 us: 1.41x faster                                                   |
| logging_silent          | 173 ns                                                 | 90.4 ns: 1.92x faster                                                   |
| logging_simple          | 8.06 us                                                | 5.76 us: 1.40x faster                                                   |
| mako                    | 14.3 ms                                                | 9.83 ms: 1.45x faster                                                   |
| mdp                     | 2.82 sec                                               | 2.57 sec: 1.10x faster                                                  |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                                    |
| mypy                    | 1.01 sec                                               | 809 ms: 1.25x faster                                                    |
| nbody                   | 136 ms                                                 | 92.8 ms: 1.47x faster                                                   |
| nqueens                 | 99.3 ms                                                | 80.6 ms: 1.23x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                   |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                   |
| pickle_dict             | 28.3 us                                                | 30.4 us: 1.07x slower                                                   |
| pickle_list             | 4.50 us                                                | 4.11 us: 1.10x faster                                                   |
| pickle_pure_python      | 453 us                                                 | 282 us: 1.61x faster                                                    |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                    |
| pprint_safe_repr        | 943 ms                                                 | 674 ms: 1.40x faster                                                    |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                  |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.32x faster                                                  |
| pyflate                 | 675 ms                                                 | 391 ms: 1.73x faster                                                    |
| python_startup          | 13.9 ms                                                | 8.48 ms: 1.64x faster                                                   |
| python_startup_no_site  | 5.76 ms                                                | 6.08 ms: 1.05x slower                                                   |
| raytrace                | 461 ms                                                 | 282 ms: 1.64x faster                                                    |
| regex_compile           | 174 ms                                                 | 131 ms: 1.32x faster                                                    |
| regex_dna               | 214 ms                                                 | 211 ms: 1.01x faster                                                    |
| regex_effbot            | 3.21 ms                                                | 3.58 ms: 1.12x slower                                                   |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                   |
| richards                | 71.4 ms                                                | 42.4 ms: 1.68x faster                                                   |
| scimark_fft             | 414 ms                                                 | 313 ms: 1.32x faster                                                    |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.48x faster                                                    |
| scimark_monte_carlo     | 105 ms                                                 | 64.4 ms: 1.63x faster                                                   |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                                    |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.10 ms: 1.34x faster                                                   |
| spectral_norm           | 148 ms                                                 | 97.5 ms: 1.52x faster                                                   |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                                   |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.41x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                    |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                                   |
| sympy_expand            | 537 ms                                                 | 456 ms: 1.18x faster                                                    |
| sympy_integrate         | 23.9 ms                                                | 20.4 ms: 1.18x faster                                                   |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.13x faster                                                    |
| sympy_str               | 324 ms                                                 | 282 ms: 1.15x faster                                                    |
| telco                   | 6.68 ms                                                | 6.41 ms: 1.04x faster                                                   |
| thrift                  | 1.03 ms                                                | 753 us: 1.37x faster                                                    |
| unpack_sequence         | 59.5 ns                                                | 41.5 ns: 1.43x faster                                                   |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                                   |
| unpickle_list           | 4.99 us                                                | 4.94 us: 1.01x faster                                                   |
| unpickle_pure_python    | 297 us                                                 | 196 us: 1.51x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                    |
| xml_etree_iterparse     | 110 ms                                                 | 104 ms: 1.06x faster                                                    |
| xml_etree_generate      | 93.3 ms                                                | 75.7 ms: 1.23x faster                                                   |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                            |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230104-3.12.0a3+-e73d0cf/bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf.json: djangocms
