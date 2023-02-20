
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 4c82d9e
- commit date: 2023-02-20
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                                |
| chameleon      | 9.17 ms                                                | 6.34 ms: 1.45x faster                                               |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.25x faster                                              |
| html5lib       | 85.9 ms                                                | 60.9 ms: 1.41x faster                                               |
| tornado_http   | 128 ms                                                 | 94.0 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.0 ms: 1.53x faster                                               |
| float          | 109 ms                                                 | 72.6 ms: 1.50x faster                                               |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                               |
| regex_dna      | 214 ms                                                 | 216 ms: 1.01x slower                                                |
| regex_effbot   | 3.19 ms                                                | 3.47 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 288 us: 1.57x faster                                                |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.64 ms: 1.39x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 54.8 ms: 1.36x faster                                               |
| json_loads           | 28.7 us                                                | 23.7 us: 1.21x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 79.7 ms: 1.18x faster                                               |
| pickle_list          | 4.72 us                                                | 4.05 us: 1.17x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| unpickle_list        | 4.92 us                                                | 4.84 us: 1.02x faster                                               |
| pickle_dict          | 27.6 us                                                | 30.2 us: 1.10x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.93 ms: 1.58x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.48 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.69 ms: 1.51x faster                                               |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                               |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                               |
| genshi_xml      | 63.7 ms                                                | 46.9 ms: 1.36x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                               |
| logging_silent          | 176 ns                                                 | 95.0 ns: 1.86x faster                                               |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                |
| asyncio_tcp             | 914 ms                                                 | 497 ms: 1.84x faster                                                |
| richards                | 75.2 ms                                                | 42.1 ms: 1.78x faster                                               |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                                |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 66.0 ms: 1.65x faster                                               |
| raytrace                | 467 ms                                                 | 288 ms: 1.62x faster                                                |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.60x faster                                               |
| spectral_norm           | 150 ms                                                 | 94.4 ms: 1.59x faster                                               |
| python_startup          | 14.1 ms                                                | 8.93 ms: 1.58x faster                                               |
| pickle_pure_python      | 452 us                                                 | 288 us: 1.57x faster                                                |
| hexiom                  | 9.43 ms                                                | 6.01 ms: 1.57x faster                                               |
| crypto_pyaes            | 117 ms                                                 | 74.6 ms: 1.56x faster                                               |
| nbody                   | 144 ms                                                 | 94.0 ms: 1.53x faster                                               |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                |
| mako                    | 14.7 ms                                                | 9.69 ms: 1.51x faster                                               |
| float                   | 109 ms                                                 | 72.6 ms: 1.50x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 35.2 us: 1.47x faster                                               |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.45x faster                                                |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                               |
| chameleon               | 9.17 ms                                                | 6.34 ms: 1.45x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.43x faster                                              |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                               |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                               |
| logging_simple          | 8.10 us                                                | 5.72 us: 1.42x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 676 ms: 1.41x faster                                                |
| html5lib                | 85.9 ms                                                | 60.9 ms: 1.41x faster                                               |
| logging_format          | 8.85 us                                                | 6.31 us: 1.40x faster                                               |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.40x faster                                              |
| json_dumps              | 13.4 ms                                                | 9.64 ms: 1.39x faster                                               |
| scimark_fft             | 421 ms                                                 | 303 ms: 1.39x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.93 ms: 1.39x faster                                               |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| async_tree_none         | 711 ms                                                 | 521 ms: 1.37x faster                                                |
| tornado_http            | 128 ms                                                 | 94.0 ms: 1.36x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 54.8 ms: 1.36x faster                                               |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                                |
| genshi_xml              | 63.7 ms                                                | 46.9 ms: 1.36x faster                                               |
| unpack_sequence         | 59.4 ns                                                | 43.9 ns: 1.35x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                              |
| aiohttp                 | 1.34 ms                                                | 998 us: 1.34x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                               |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                                |
| async_tree_memoization  | 855 ms                                                 | 645 ms: 1.33x faster                                                |
| deepcopy                | 438 us                                                 | 335 us: 1.31x faster                                                |
| mypy2                   | 430 ms                                                 | 329 ms: 1.31x faster                                                |
| fannkuch                | 488 ms                                                 | 374 ms: 1.30x faster                                                |
| deepcopy_reduce         | 3.79 us                                                | 2.94 us: 1.29x faster                                               |
| sqlglot_optimize        | 65.2 ms                                                | 51.2 ms: 1.28x faster                                               |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed | 949 ms                                                 | 748 ms: 1.27x faster                                                |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.25x faster                                              |
| nqueens                 | 100 ms                                                 | 80.2 ms: 1.25x faster                                               |
| coroutines              | 31.6 ms                                                | 25.4 ms: 1.25x faster                                               |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                               |
| json_loads              | 28.7 us                                                | 23.7 us: 1.21x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                |
| dulwich_log             | 75.8 ms                                                | 62.7 ms: 1.21x faster                                               |
| bench_thread_pool       | 946 us                                                 | 786 us: 1.20x faster                                                |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.2 ms: 1.18x faster                                               |
| xml_etree_generate      | 93.8 ms                                                | 79.7 ms: 1.18x faster                                               |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.17x faster                                                |
| pickle_list             | 4.72 us                                                | 4.05 us: 1.17x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.16x faster                                               |
| sympy_expand            | 534 ms                                                 | 462 ms: 1.16x faster                                                |
| json                    | 5.35 ms                                                | 4.68 ms: 1.14x faster                                               |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.13x faster                                               |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| mdp                     | 2.74 sec                                               | 2.48 sec: 1.10x faster                                              |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| telco                   | 6.73 ms                                                | 6.54 ms: 1.03x faster                                               |
| unpickle_list           | 4.92 us                                                | 4.84 us: 1.02x faster                                               |
| regex_dna               | 214 ms                                                 | 216 ms: 1.01x slower                                                |
| generators              | 76.4 ms                                                | 77.3 ms: 1.01x slower                                               |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                |
| regex_effbot            | 3.19 ms                                                | 3.47 ms: 1.08x slower                                               |
| pickle_dict             | 27.6 us                                                | 30.2 us: 1.10x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.48 ms: 1.12x slower                                               |
| gc_traversal            | 3.53 ms                                                | 4.17 ms: 1.18x slower                                               |
| coverage                | 74.7 ms                                                | 100.0 ms: 1.34x slower                                              |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                        |

Benchmark hidden because not significant (3): bench_mp_pool, async_generators, pickle
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
