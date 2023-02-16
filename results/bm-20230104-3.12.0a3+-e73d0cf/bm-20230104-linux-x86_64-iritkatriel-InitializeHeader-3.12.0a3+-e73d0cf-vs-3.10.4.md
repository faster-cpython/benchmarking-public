
# Results vs. 3.10.4

- fork: iritkatriel
- ref: InitializeHeader
- machine: linux-x86_64
- commit hash: e73d0cf
- commit date: 2023-01-04
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                    |
| chameleon      | 9.17 ms                                                | 6.17 ms: 1.49x faster                                                   |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                  |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.38x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 92.8 ms: 1.55x faster                                                   |
| float          | 109 ms                                                 | 71.7 ms: 1.52x faster                                                   |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.32x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                                    |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                   |
| regex_dna      | 214 ms                                                 | 211 ms: 1.01x faster                                                    |
| regex_effbot   | 3.19 ms                                                | 3.58 ms: 1.12x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                                    |
| unpickle_pure_python | 302 us                                                 | 196 us: 1.53x faster                                                    |
| json_dumps           | 13.4 ms                                                | 9.42 ms: 1.43x faster                                                   |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                   |
| xml_etree_generate   | 93.8 ms                                                | 75.7 ms: 1.24x faster                                                   |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                                   |
| pickle_list          | 4.72 us                                                | 4.11 us: 1.15x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                    |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.06x faster                                                    |
| pickle_dict          | 27.6 us                                                | 30.4 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                            |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.48 ms: 1.66x faster                                                   |
| python_startup_no_site | 5.78 ms                                                | 6.08 ms: 1.05x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                   |
| mako            | 14.7 ms                                                | 9.83 ms: 1.49x faster                                                   |
| django_template | 46.3 ms                                                | 32.3 ms: 1.44x faster                                                   |
| genshi_xml      | 63.7 ms                                                | 46.3 ms: 1.38x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.34 ms: 2.18x faster                                                   |
| logging_silent          | 176 ns                                                 | 90.4 ns: 1.95x faster                                                   |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.85x faster                                                    |
| richards                | 75.2 ms                                                | 42.4 ms: 1.77x faster                                                   |
| pyflate                 | 676 ms                                                 | 391 ms: 1.73x faster                                                    |
| scimark_monte_carlo     | 109 ms                                                 | 64.4 ms: 1.69x faster                                                   |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                    |
| python_startup          | 14.1 ms                                                | 8.48 ms: 1.66x faster                                                   |
| raytrace                | 467 ms                                                 | 282 ms: 1.66x faster                                                    |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                                    |
| crypto_pyaes            | 117 ms                                                 | 73.5 ms: 1.59x faster                                                   |
| chaos                   | 106 ms                                                 | 67.9 ms: 1.56x faster                                                   |
| nbody                   | 144 ms                                                 | 92.8 ms: 1.55x faster                                                   |
| hexiom                  | 9.43 ms                                                | 6.09 ms: 1.55x faster                                                   |
| unpickle_pure_python    | 302 us                                                 | 196 us: 1.53x faster                                                    |
| deepcopy_memo           | 51.7 us                                                | 33.7 us: 1.53x faster                                                   |
| spectral_norm           | 150 ms                                                 | 97.5 ms: 1.53x faster                                                   |
| float                   | 109 ms                                                 | 71.7 ms: 1.52x faster                                                   |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                                    |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                   |
| mako                    | 14.7 ms                                                | 9.83 ms: 1.49x faster                                                   |
| chameleon               | 9.17 ms                                                | 6.17 ms: 1.49x faster                                                   |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                   |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                                  |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.44x faster                                                   |
| unpack_sequence         | 59.4 ns                                                | 41.5 ns: 1.43x faster                                                   |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                   |
| json_dumps              | 13.4 ms                                                | 9.42 ms: 1.43x faster                                                   |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                   |
| pprint_safe_repr        | 953 ms                                                 | 674 ms: 1.41x faster                                                    |
| logging_simple          | 8.10 us                                                | 5.76 us: 1.41x faster                                                   |
| logging_format          | 8.85 us                                                | 6.35 us: 1.39x faster                                                   |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                   |
| genshi_xml              | 63.7 ms                                                | 46.3 ms: 1.38x faster                                                   |
| thrift                  | 1.03 ms                                                | 753 us: 1.37x faster                                                    |
| async_tree_memoization  | 855 ms                                                 | 623 ms: 1.37x faster                                                    |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                    |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                  |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                                    |
| scimark_fft             | 421 ms                                                 | 313 ms: 1.35x faster                                                    |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                  |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.10 ms: 1.33x faster                                                   |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                                    |
| fannkuch                | 488 ms                                                 | 368 ms: 1.32x faster                                                    |
| deepcopy_reduce         | 3.79 us                                                | 2.90 us: 1.31x faster                                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.8 ms: 1.28x faster                                                   |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                    |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                  |
| coroutines              | 31.6 ms                                                | 25.0 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 750 ms: 1.26x faster                                                    |
| nqueens                 | 100 ms                                                 | 80.6 ms: 1.24x faster                                                   |
| xml_etree_generate      | 93.8 ms                                                | 75.7 ms: 1.24x faster                                                   |
| dulwich_log             | 75.8 ms                                                | 62.0 ms: 1.22x faster                                                   |
| bench_thread_pool       | 946 us                                                 | 774 us: 1.22x faster                                                    |
| async_generators        | 426 ms                                                 | 355 ms: 1.20x faster                                                    |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                                   |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                                   |
| sympy_expand            | 534 ms                                                 | 456 ms: 1.17x faster                                                    |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                                    |
| pickle_list             | 4.72 us                                                | 4.11 us: 1.15x faster                                                   |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                                   |
| json                    | 5.35 ms                                                | 4.73 ms: 1.13x faster                                                   |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                   |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.12x faster                                                    |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                    |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                                    |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                                   |
| mdp                     | 2.74 sec                                               | 2.57 sec: 1.07x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.06x faster                                                    |
| telco                   | 6.73 ms                                                | 6.41 ms: 1.05x faster                                                   |
| regex_dna               | 214 ms                                                 | 211 ms: 1.01x faster                                                    |
| generators              | 76.4 ms                                                | 77.1 ms: 1.01x slower                                                   |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                    |
| python_startup_no_site  | 5.78 ms                                                | 6.08 ms: 1.05x slower                                                   |
| pickle_dict             | 27.6 us                                                | 30.4 us: 1.10x slower                                                   |
| regex_effbot            | 3.19 ms                                                | 3.58 ms: 1.12x slower                                                   |
| coverage                | 74.7 ms                                                | 98.7 ms: 1.32x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                            |

Benchmark hidden because not significant (3): bench_mp_pool, unpickle_list, pickle
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230104-3.12.0a3+-e73d0cf/bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf.json: mypy
