
# Results vs. 3.11.0

- fork: iritkatriel
- ref: InitializeHeader
- machine: linux-x86_64
- commit hash: e73d0cf
- commit date: 2023-01-04
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                    |
| chameleon      | 6.41 ms                                                | 6.17 ms: 1.04x faster                                                   |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                  |
| html5lib       | 63.2 ms                                                | 60.1 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.7 ms: 1.06x faster                                                   |
| nbody          | 95.0 ms                                                | 92.8 ms: 1.02x faster                                                   |
| pidigits       | 199 ms                                                 | 192 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                                    |
| regex_dna      | 203 ms                                                 | 211 ms: 1.04x slower                                                    |
| regex_effbot   | 3.36 ms                                                | 3.58 ms: 1.07x slower                                                   |
| regex_v8       | 22.3 ms                                                | 22.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.42 ms: 1.34x faster                                                   |
| json_loads           | 26.2 us                                                | 24.0 us: 1.09x faster                                                   |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                                   |
| pickle_dict          | 31.4 us                                                | 30.4 us: 1.03x faster                                                   |
| pickle_list          | 4.17 us                                                | 4.11 us: 1.02x faster                                                   |
| pickle_pure_python   | 304 us                                                 | 282 us: 1.08x faster                                                    |
| unpickle_pure_python | 225 us                                                 | 196 us: 1.15x faster                                                    |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 103 ms                                                 | 104 ms: 1.02x slower                                                    |
| xml_etree_generate   | 76.2 ms                                                | 75.7 ms: 1.01x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (3): unpickle, unpickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.48 ms: 1.02x slower                                                   |
| python_startup_no_site | 5.96 ms                                                | 6.08 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 32.3 ms: 1.01x faster                                                   |
| genshi_text     | 22.1 ms                                                | 20.4 ms: 1.08x faster                                                   |
| genshi_xml      | 52.1 ms                                                | 46.3 ms: 1.12x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                    |
| async_generators        | 359 ms                                                 | 355 ms: 1.01x faster                                                    |
| async_tree_none         | 529 ms                                                 | 524 ms: 1.01x faster                                                    |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                  |
| chameleon               | 6.41 ms                                                | 6.17 ms: 1.04x faster                                                   |
| chaos                   | 68.6 ms                                                | 67.9 ms: 1.01x faster                                                   |
| bench_thread_pool       | 810 us                                                 | 774 us: 1.05x faster                                                    |
| coroutines              | 26.1 ms                                                | 25.0 ms: 1.04x faster                                                   |
| coverage                | 101 ms                                                 | 98.7 ms: 1.02x faster                                                   |
| crypto_pyaes            | 73.9 ms                                                | 73.5 ms: 1.01x faster                                                   |
| deepcopy                | 344 us                                                 | 330 us: 1.04x faster                                                    |
| deepcopy_reduce         | 2.97 us                                                | 2.90 us: 1.02x faster                                                   |
| deepcopy_memo           | 36.4 us                                                | 33.7 us: 1.08x faster                                                   |
| deltablue               | 3.64 ms                                                | 3.34 ms: 1.09x faster                                                   |
| django_template         | 32.5 ms                                                | 32.3 ms: 1.01x faster                                                   |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                  |
| dulwich_log             | 63.9 ms                                                | 62.0 ms: 1.03x faster                                                   |
| fannkuch                | 388 ms                                                 | 368 ms: 1.05x faster                                                    |
| float                   | 76.3 ms                                                | 71.7 ms: 1.06x faster                                                   |
| generators              | 72.2 ms                                                | 77.1 ms: 1.07x slower                                                   |
| genshi_text             | 22.1 ms                                                | 20.4 ms: 1.08x faster                                                   |
| genshi_xml              | 52.1 ms                                                | 46.3 ms: 1.12x faster                                                   |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                                    |
| hexiom                  | 6.35 ms                                                | 6.09 ms: 1.04x faster                                                   |
| html5lib                | 63.2 ms                                                | 60.1 ms: 1.05x faster                                                   |
| json                    | 4.95 ms                                                | 4.73 ms: 1.05x faster                                                   |
| json_dumps              | 12.7 ms                                                | 9.42 ms: 1.34x faster                                                   |
| json_loads              | 26.2 us                                                | 24.0 us: 1.09x faster                                                   |
| logging_format          | 6.62 us                                                | 6.35 us: 1.04x faster                                                   |
| logging_silent          | 98.5 ns                                                | 90.4 ns: 1.09x faster                                                   |
| logging_simple          | 6.06 us                                                | 5.76 us: 1.05x faster                                                   |
| mdp                     | 2.62 sec                                               | 2.57 sec: 1.02x faster                                                  |
| mypy                    | 669 ms                                                 | 809 ms: 1.21x slower                                                    |
| nbody                   | 95.0 ms                                                | 92.8 ms: 1.02x faster                                                   |
| nqueens                 | 85.0 ms                                                | 80.6 ms: 1.05x faster                                                   |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                                   |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                                   |
| pickle_dict             | 31.4 us                                                | 30.4 us: 1.03x faster                                                   |
| pickle_list             | 4.17 us                                                | 4.11 us: 1.02x faster                                                   |
| pickle_pure_python      | 304 us                                                 | 282 us: 1.08x faster                                                    |
| pidigits                | 199 ms                                                 | 192 ms: 1.04x faster                                                    |
| pprint_safe_repr        | 691 ms                                                 | 674 ms: 1.02x faster                                                    |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.05x faster                                                  |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                                  |
| pyflate                 | 417 ms                                                 | 391 ms: 1.07x faster                                                    |
| python_startup          | 8.36 ms                                                | 8.48 ms: 1.02x slower                                                   |
| python_startup_no_site  | 5.96 ms                                                | 6.08 ms: 1.02x slower                                                   |
| raytrace                | 290 ms                                                 | 282 ms: 1.03x faster                                                    |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                                    |
| regex_dna               | 203 ms                                                 | 211 ms: 1.04x slower                                                    |
| regex_effbot            | 3.36 ms                                                | 3.58 ms: 1.07x slower                                                   |
| regex_v8                | 22.3 ms                                                | 22.5 ms: 1.01x slower                                                   |
| richards                | 46.2 ms                                                | 42.4 ms: 1.09x faster                                                   |
| scimark_fft             | 329 ms                                                 | 313 ms: 1.05x faster                                                    |
| scimark_monte_carlo     | 68.3 ms                                                | 64.4 ms: 1.06x faster                                                   |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.10 ms: 1.07x faster                                                   |
| spectral_norm           | 99.9 ms                                                | 97.5 ms: 1.02x faster                                                   |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                   |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                                   |
| sqlglot_optimize        | 53.0 ms                                                | 50.8 ms: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                    |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                                   |
| sympy_expand            | 472 ms                                                 | 456 ms: 1.03x faster                                                    |
| sympy_integrate         | 20.9 ms                                                | 20.4 ms: 1.02x faster                                                   |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                                    |
| sympy_str               | 287 ms                                                 | 282 ms: 1.02x faster                                                    |
| telco                   | 6.62 ms                                                | 6.41 ms: 1.03x faster                                                   |
| unpack_sequence         | 43.4 ns                                                | 41.5 ns: 1.05x faster                                                   |
| unpickle_pure_python    | 225 us                                                 | 196 us: 1.15x faster                                                    |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                    |
| xml_etree_iterparse     | 103 ms                                                 | 104 ms: 1.02x slower                                                    |
| xml_etree_generate      | 76.2 ms                                                | 75.7 ms: 1.01x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, async_tree_memoization, bench_mp_pool, mako, meteor_contest, scimark_lu, thrift, unpickle, unpickle_list, xml_etree_process
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/mdboom/Work/builds/benchmarking/results/bm-20230104-3.12.0a3+-e73d0cf/bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf.json: djangocms
