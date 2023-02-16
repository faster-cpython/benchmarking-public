
# Results vs. 3.10.4

- fork: iritkatriel
- ref: object_init
- machine: linux-x86_64
- commit hash: 1a4b9a9
- commit date: 2023-02-08
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                               |
| chameleon      | 9.17 ms                                                | 6.36 ms: 1.44x faster                                              |
| docutils       | 3.18 sec                                               | 2.56 sec: 1.24x faster                                             |
| html5lib       | 85.9 ms                                                | 60.9 ms: 1.41x faster                                              |
| tornado_http   | 128 ms                                                 | 94.0 ms: 1.36x faster                                              |
| Geometric mean | (ref)                                                  | 1.36x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 86.0 ms: 1.67x faster                                              |
| float          | 109 ms                                                 | 72.1 ms: 1.51x faster                                              |
| Geometric mean | (ref)                                                  | 1.36x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                               |
| regex_v8       | 25.0 ms                                                | 21.4 ms: 1.17x faster                                              |
| regex_dna      | 214 ms                                                 | 211 ms: 1.01x faster                                               |
| regex_effbot   | 3.19 ms                                                | 3.32 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 288 us: 1.57x faster                                               |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                               |
| json_dumps           | 13.4 ms                                                | 9.34 ms: 1.44x faster                                              |
| xml_etree_process    | 74.5 ms                                                | 55.6 ms: 1.34x faster                                              |
| json_loads           | 28.7 us                                                | 23.7 us: 1.21x faster                                              |
| pickle_list          | 4.72 us                                                | 4.09 us: 1.16x faster                                              |
| xml_etree_generate   | 93.8 ms                                                | 81.3 ms: 1.15x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                               |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 108 ms: 1.02x faster                                               |
| unpickle_list        | 4.92 us                                                | 5.04 us: 1.02x slower                                              |
| pickle_dict          | 27.6 us                                                | 30.6 us: 1.11x slower                                              |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                       |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.97 ms: 1.57x faster                                              |
| python_startup_no_site | 5.78 ms                                                | 6.51 ms: 1.13x slower                                              |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.65 ms: 1.52x faster                                              |
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                              |
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                              |
| genshi_xml      | 63.7 ms                                                | 46.4 ms: 1.37x faster                                              |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.18 ms: 2.29x faster                                              |
| logging_silent          | 176 ns                                                 | 92.3 ns: 1.91x faster                                              |
| asyncio_tcp             | 914 ms                                                 | 490 ms: 1.87x faster                                               |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.83x faster                                               |
| richards                | 75.2 ms                                                | 42.2 ms: 1.78x faster                                              |
| pyflate                 | 676 ms                                                 | 403 ms: 1.68x faster                                               |
| nbody                   | 144 ms                                                 | 86.0 ms: 1.67x faster                                              |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                               |
| scimark_monte_carlo     | 109 ms                                                 | 65.0 ms: 1.67x faster                                              |
| raytrace                | 467 ms                                                 | 281 ms: 1.66x faster                                               |
| chaos                   | 106 ms                                                 | 64.1 ms: 1.65x faster                                              |
| crypto_pyaes            | 117 ms                                                 | 71.3 ms: 1.64x faster                                              |
| hexiom                  | 9.43 ms                                                | 5.95 ms: 1.59x faster                                              |
| python_startup          | 14.1 ms                                                | 8.97 ms: 1.57x faster                                              |
| pickle_pure_python      | 452 us                                                 | 288 us: 1.57x faster                                               |
| spectral_norm           | 150 ms                                                 | 95.9 ms: 1.56x faster                                              |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 33.9 us: 1.52x faster                                              |
| mako                    | 14.7 ms                                                | 9.65 ms: 1.52x faster                                              |
| float                   | 109 ms                                                 | 72.1 ms: 1.51x faster                                              |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.51x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                              |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                              |
| chameleon               | 9.17 ms                                                | 6.36 ms: 1.44x faster                                              |
| json_dumps              | 13.4 ms                                                | 9.34 ms: 1.44x faster                                              |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                              |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                             |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                              |
| scimark_fft             | 421 ms                                                 | 298 ms: 1.41x faster                                               |
| html5lib                | 85.9 ms                                                | 60.9 ms: 1.41x faster                                              |
| pprint_safe_repr        | 953 ms                                                 | 680 ms: 1.40x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.90 ms: 1.40x faster                                              |
| logging_simple          | 8.10 us                                                | 5.79 us: 1.40x faster                                              |
| logging_format          | 8.85 us                                                | 6.34 us: 1.40x faster                                              |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                             |
| unpack_sequence         | 59.4 ns                                                | 42.6 ns: 1.39x faster                                              |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                               |
| genshi_xml              | 63.7 ms                                                | 46.4 ms: 1.37x faster                                              |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                             |
| tornado_http            | 128 ms                                                 | 94.0 ms: 1.36x faster                                              |
| async_tree_none         | 711 ms                                                 | 523 ms: 1.36x faster                                               |
| thrift                  | 1.03 ms                                                | 765 us: 1.35x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 635 ms: 1.35x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 55.6 ms: 1.34x faster                                              |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                               |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                              |
| deepcopy                | 438 us                                                 | 328 us: 1.33x faster                                               |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                              |
| fannkuch                | 488 ms                                                 | 369 ms: 1.32x faster                                               |
| mypy2                   | 430 ms                                                 | 328 ms: 1.31x faster                                               |
| deepcopy_reduce         | 3.79 us                                                | 2.92 us: 1.30x faster                                              |
| coroutines              | 31.6 ms                                                | 24.5 ms: 1.29x faster                                              |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                              |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                               |
| nqueens                 | 100 ms                                                 | 78.8 ms: 1.27x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 752 ms: 1.26x faster                                               |
| docutils                | 3.18 sec                                               | 2.56 sec: 1.24x faster                                             |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                              |
| json_loads              | 28.7 us                                                | 23.7 us: 1.21x faster                                              |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                               |
| bench_thread_pool       | 946 us                                                 | 786 us: 1.20x faster                                               |
| dulwich_log             | 75.8 ms                                                | 63.1 ms: 1.20x faster                                              |
| sympy_str               | 325 ms                                                 | 271 ms: 1.20x faster                                               |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                              |
| regex_v8                | 25.0 ms                                                | 21.4 ms: 1.17x faster                                              |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                               |
| djangocms               | 36.9 us                                                | 31.6 us: 1.17x faster                                              |
| sympy_sum               | 183 ms                                                 | 158 ms: 1.16x faster                                               |
| pickle_list             | 4.72 us                                                | 4.09 us: 1.16x faster                                              |
| xml_etree_generate      | 93.8 ms                                                | 81.3 ms: 1.15x faster                                              |
| json                    | 5.35 ms                                                | 4.64 ms: 1.15x faster                                              |
| sqlite_synth            | 2.92 us                                                | 2.56 us: 1.14x faster                                              |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                              |
| mdp                     | 2.74 sec                                               | 2.45 sec: 1.12x faster                                             |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                               |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                              |
| meteor_contest          | 114 ms                                                 | 107 ms: 1.06x faster                                               |
| telco                   | 6.73 ms                                                | 6.40 ms: 1.05x faster                                              |
| xml_etree_iterparse     | 111 ms                                                 | 108 ms: 1.02x faster                                               |
| regex_dna               | 214 ms                                                 | 211 ms: 1.01x faster                                               |
| async_generators        | 426 ms                                                 | 423 ms: 1.01x faster                                               |
| unpickle_list           | 4.92 us                                                | 5.04 us: 1.02x slower                                              |
| regex_effbot            | 3.19 ms                                                | 3.32 ms: 1.04x slower                                              |
| pickle_dict             | 27.6 us                                                | 30.6 us: 1.11x slower                                              |
| gc_traversal            | 3.53 ms                                                | 3.96 ms: 1.12x slower                                              |
| python_startup_no_site  | 5.78 ms                                                | 6.51 ms: 1.13x slower                                              |
| coverage                | 74.7 ms                                                | 97.3 ms: 1.30x slower                                              |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                       |

Benchmark hidden because not significant (4): pidigits, bench_mp_pool, generators, pickle
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
