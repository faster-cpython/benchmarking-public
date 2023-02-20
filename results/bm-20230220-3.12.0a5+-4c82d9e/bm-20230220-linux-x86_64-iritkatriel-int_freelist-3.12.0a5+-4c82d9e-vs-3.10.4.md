
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 4c82d9e
- commit date: 2023-02-20
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                                |
| chameleon      | 9.17 ms                                                | 6.25 ms: 1.47x faster                                               |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.25x faster                                              |
| html5lib       | 85.9 ms                                                | 61.7 ms: 1.39x faster                                               |
| tornado_http   | 128 ms                                                 | 93.8 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.6 ms: 1.52x faster                                               |
| float          | 109 ms                                                 | 72.2 ms: 1.51x faster                                               |
| pidigits       | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                               |
| regex_dna      | 214 ms                                                 | 199 ms: 1.08x faster                                                |
| regex_effbot   | 3.19 ms                                                | 3.46 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 290 us: 1.56x faster                                                |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.44 ms: 1.42x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 57.2 ms: 1.30x faster                                               |
| json_loads           | 28.7 us                                                | 23.8 us: 1.20x faster                                               |
| pickle_list          | 4.72 us                                                | 4.08 us: 1.16x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 82.2 ms: 1.14x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| unpickle_list        | 4.92 us                                                | 4.80 us: 1.03x faster                                               |
| pickle               | 10.2 us                                                | 10.0 us: 1.01x faster                                               |
| pickle_dict          | 27.6 us                                                | 29.7 us: 1.08x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.95 ms: 1.57x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.50 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.51 ms: 1.54x faster                                               |
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                               |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                               |
| genshi_xml      | 63.7 ms                                                | 47.6 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.27x faster                                               |
| logging_silent          | 176 ns                                                 | 91.6 ns: 1.93x faster                                               |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.87x faster                                                |
| asyncio_tcp             | 914 ms                                                 | 496 ms: 1.84x faster                                                |
| richards                | 75.2 ms                                                | 42.0 ms: 1.79x faster                                               |
| pyflate                 | 676 ms                                                 | 398 ms: 1.70x faster                                                |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 65.3 ms: 1.66x faster                                               |
| raytrace                | 467 ms                                                 | 281 ms: 1.66x faster                                                |
| chaos                   | 106 ms                                                 | 65.0 ms: 1.62x faster                                               |
| spectral_norm           | 150 ms                                                 | 93.8 ms: 1.59x faster                                               |
| hexiom                  | 9.43 ms                                                | 5.98 ms: 1.58x faster                                               |
| python_startup          | 14.1 ms                                                | 8.95 ms: 1.57x faster                                               |
| pickle_pure_python      | 452 us                                                 | 290 us: 1.56x faster                                                |
| mako                    | 14.7 ms                                                | 9.51 ms: 1.54x faster                                               |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                |
| crypto_pyaes            | 117 ms                                                 | 76.4 ms: 1.53x faster                                               |
| nbody                   | 144 ms                                                 | 94.6 ms: 1.52x faster                                               |
| float                   | 109 ms                                                 | 72.2 ms: 1.51x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                               |
| chameleon               | 9.17 ms                                                | 6.25 ms: 1.47x faster                                               |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.45x faster                                                |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                               |
| json_dumps              | 13.4 ms                                                | 9.44 ms: 1.42x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.42x faster                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                               |
| logging_format          | 8.85 us                                                | 6.27 us: 1.41x faster                                               |
| logging_simple          | 8.10 us                                                | 5.75 us: 1.41x faster                                               |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                               |
| unpack_sequence         | 59.4 ns                                                | 42.5 ns: 1.40x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 685 ms: 1.39x faster                                                |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                              |
| scimark_fft             | 421 ms                                                 | 303 ms: 1.39x faster                                                |
| html5lib                | 85.9 ms                                                | 61.7 ms: 1.39x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.96 ms: 1.38x faster                                               |
| tornado_http            | 128 ms                                                 | 93.8 ms: 1.37x faster                                               |
| thrift                  | 1.03 ms                                                | 758 us: 1.36x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                              |
| aiohttp                 | 1.34 ms                                                | 997 us: 1.34x faster                                                |
| genshi_xml              | 63.7 ms                                                | 47.6 ms: 1.34x faster                                               |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                               |
| async_tree_none         | 711 ms                                                 | 532 ms: 1.34x faster                                                |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                                |
| fannkuch                | 488 ms                                                 | 370 ms: 1.32x faster                                                |
| deepcopy                | 438 us                                                 | 332 us: 1.32x faster                                                |
| xml_etree_process       | 74.5 ms                                                | 57.2 ms: 1.30x faster                                               |
| mypy2                   | 430 ms                                                 | 331 ms: 1.30x faster                                                |
| deepcopy_reduce         | 3.79 us                                                | 2.93 us: 1.29x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 666 ms: 1.28x faster                                                |
| nqueens                 | 100 ms                                                 | 78.2 ms: 1.28x faster                                               |
| sqlglot_optimize        | 65.2 ms                                                | 51.7 ms: 1.26x faster                                               |
| sqlglot_normalize       | 134 ms                                                 | 107 ms: 1.26x faster                                                |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.25x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 759 ms: 1.25x faster                                                |
| coroutines              | 31.6 ms                                                | 25.7 ms: 1.23x faster                                               |
| dulwich_log             | 75.8 ms                                                | 62.0 ms: 1.22x faster                                               |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                |
| bench_thread_pool       | 946 us                                                 | 783 us: 1.21x faster                                                |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                |
| json_loads              | 28.7 us                                                | 23.8 us: 1.20x faster                                               |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.9 ms: 1.20x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                               |
| sympy_expand            | 534 ms                                                 | 458 ms: 1.17x faster                                                |
| sympy_sum               | 183 ms                                                 | 158 ms: 1.16x faster                                                |
| pickle_list             | 4.72 us                                                | 4.08 us: 1.16x faster                                               |
| json                    | 5.35 ms                                                | 4.63 ms: 1.15x faster                                               |
| djangocms               | 36.9 us                                                | 32.2 us: 1.14x faster                                               |
| sqlite_synth            | 2.92 us                                                | 2.56 us: 1.14x faster                                               |
| xml_etree_generate      | 93.8 ms                                                | 82.2 ms: 1.14x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| mdp                     | 2.74 sec                                               | 2.52 sec: 1.09x faster                                              |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                                |
| regex_dna               | 214 ms                                                 | 199 ms: 1.08x faster                                                |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| telco                   | 6.73 ms                                                | 6.38 ms: 1.06x faster                                               |
| unpickle_list           | 4.92 us                                                | 4.80 us: 1.03x faster                                               |
| pickle                  | 10.2 us                                                | 10.0 us: 1.01x faster                                               |
| async_generators        | 426 ms                                                 | 423 ms: 1.01x faster                                                |
| pidigits                | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| generators              | 76.4 ms                                                | 77.3 ms: 1.01x slower                                               |
| pickle_dict             | 27.6 us                                                | 29.7 us: 1.08x slower                                               |
| regex_effbot            | 3.19 ms                                                | 3.46 ms: 1.08x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.50 ms: 1.13x slower                                               |
| gc_traversal            | 3.53 ms                                                | 4.29 ms: 1.22x slower                                               |
| coverage                | 74.7 ms                                                | 97.9 ms: 1.31x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
