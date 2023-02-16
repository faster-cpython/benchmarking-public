
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 827b81b
- commit date: 2023-02-09
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| chameleon      | 9.17 ms                                                | 6.39 ms: 1.43x faster                                               |
| docutils       | 3.18 sec                                               | 2.54 sec: 1.25x faster                                              |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                               |
| tornado_http   | 128 ms                                                 | 93.9 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.5 ms: 1.52x faster                                               |
| float          | 109 ms                                                 | 73.0 ms: 1.49x faster                                               |
| pidigits       | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.31x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.4 ms: 1.17x faster                                               |
| regex_dna      | 214 ms                                                 | 218 ms: 1.02x slower                                                |
| regex_effbot   | 3.19 ms                                                | 3.46 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 289 us: 1.56x faster                                                |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.58 ms: 1.40x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 54.9 ms: 1.36x faster                                               |
| json_loads           | 28.7 us                                                | 24.0 us: 1.19x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 80.4 ms: 1.17x faster                                               |
| pickle_list          | 4.72 us                                                | 4.21 us: 1.12x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| unpickle_list        | 4.92 us                                                | 4.88 us: 1.01x faster                                               |
| pickle_dict          | 27.6 us                                                | 31.2 us: 1.13x slower                                               |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.93 ms: 1.58x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.47 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.73 ms: 1.51x faster                                               |
| genshi_text     | 30.6 ms                                                | 21.0 ms: 1.46x faster                                               |
| django_template | 46.3 ms                                                | 33.6 ms: 1.38x faster                                               |
| genshi_xml      | 63.7 ms                                                | 47.1 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.22 ms: 2.26x faster                                               |
| logging_silent          | 176 ns                                                 | 93.2 ns: 1.89x faster                                               |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                |
| asyncio_tcp             | 914 ms                                                 | 498 ms: 1.84x faster                                                |
| richards                | 75.2 ms                                                | 43.3 ms: 1.74x faster                                               |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                |
| pyflate                 | 676 ms                                                 | 407 ms: 1.66x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 65.9 ms: 1.65x faster                                               |
| raytrace                | 467 ms                                                 | 286 ms: 1.63x faster                                                |
| chaos                   | 106 ms                                                 | 65.6 ms: 1.61x faster                                               |
| hexiom                  | 9.43 ms                                                | 5.97 ms: 1.58x faster                                               |
| python_startup          | 14.1 ms                                                | 8.93 ms: 1.58x faster                                               |
| pickle_pure_python      | 452 us                                                 | 289 us: 1.56x faster                                                |
| nbody                   | 144 ms                                                 | 94.5 ms: 1.52x faster                                               |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                |
| spectral_norm           | 150 ms                                                 | 98.5 ms: 1.52x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.2 us: 1.51x faster                                               |
| mako                    | 14.7 ms                                                | 9.73 ms: 1.51x faster                                               |
| crypto_pyaes            | 117 ms                                                 | 77.7 ms: 1.50x faster                                               |
| float                   | 109 ms                                                 | 73.0 ms: 1.49x faster                                               |
| genshi_text             | 30.6 ms                                                | 21.0 ms: 1.46x faster                                               |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.44x faster                                                |
| chameleon               | 9.17 ms                                                | 6.39 ms: 1.43x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                               |
| logging_simple          | 8.10 us                                                | 5.74 us: 1.41x faster                                               |
| sqlglot_transpile       | 2.43 ms                                                | 1.73 ms: 1.41x faster                                               |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.41x faster                                              |
| unpack_sequence         | 59.4 ns                                                | 42.3 ns: 1.41x faster                                               |
| json_dumps              | 13.4 ms                                                | 9.58 ms: 1.40x faster                                               |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                               |
| scimark_fft             | 421 ms                                                 | 302 ms: 1.39x faster                                                |
| logging_format          | 8.85 us                                                | 6.36 us: 1.39x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.42 sec: 1.39x faster                                              |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                                |
| django_template         | 46.3 ms                                                | 33.6 ms: 1.38x faster                                               |
| thrift                  | 1.03 ms                                                | 756 us: 1.37x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.99 ms: 1.37x faster                                               |
| tornado_http            | 128 ms                                                 | 93.9 ms: 1.37x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 699 ms: 1.36x faster                                                |
| xml_etree_process       | 74.5 ms                                                | 54.9 ms: 1.36x faster                                               |
| genshi_xml              | 63.7 ms                                                | 47.1 ms: 1.35x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                              |
| async_tree_none         | 711 ms                                                 | 527 ms: 1.35x faster                                                |
| fannkuch                | 488 ms                                                 | 364 ms: 1.34x faster                                                |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                               |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 649 ms: 1.32x faster                                                |
| mypy2                   | 430 ms                                                 | 330 ms: 1.30x faster                                                |
| deepcopy_reduce         | 3.79 us                                                | 2.92 us: 1.30x faster                                               |
| nqueens                 | 100 ms                                                 | 78.1 ms: 1.28x faster                                               |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.26x faster                                                |
| sqlglot_optimize        | 65.2 ms                                                | 51.7 ms: 1.26x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                |
| docutils                | 3.18 sec                                               | 2.54 sec: 1.25x faster                                              |
| coroutines              | 31.6 ms                                                | 25.5 ms: 1.24x faster                                               |
| dulwich_log             | 75.8 ms                                                | 62.4 ms: 1.22x faster                                               |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                               |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.8 ms: 1.21x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                |
| bench_thread_pool       | 946 us                                                 | 785 us: 1.21x faster                                                |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                |
| json_loads              | 28.7 us                                                | 24.0 us: 1.19x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.4 ms: 1.17x faster                                               |
| xml_etree_generate      | 93.8 ms                                                | 80.4 ms: 1.17x faster                                               |
| sympy_sum               | 183 ms                                                 | 158 ms: 1.16x faster                                                |
| sympy_expand            | 534 ms                                                 | 459 ms: 1.16x faster                                                |
| json                    | 5.35 ms                                                | 4.64 ms: 1.15x faster                                               |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                               |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                               |
| pickle_list             | 4.72 us                                                | 4.21 us: 1.12x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| mdp                     | 2.74 sec                                               | 2.49 sec: 1.10x faster                                              |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| telco                   | 6.73 ms                                                | 6.49 ms: 1.04x faster                                               |
| unpickle_list           | 4.92 us                                                | 4.88 us: 1.01x faster                                               |
| async_generators        | 426 ms                                                 | 424 ms: 1.01x faster                                                |
| pidigits                | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| generators              | 76.4 ms                                                | 77.7 ms: 1.02x slower                                               |
| regex_dna               | 214 ms                                                 | 218 ms: 1.02x slower                                                |
| regex_effbot            | 3.19 ms                                                | 3.46 ms: 1.08x slower                                               |
| gc_traversal            | 3.53 ms                                                | 3.85 ms: 1.09x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.47 ms: 1.12x slower                                               |
| pickle_dict             | 27.6 us                                                | 31.2 us: 1.13x slower                                               |
| coverage                | 74.7 ms                                                | 97.9 ms: 1.31x slower                                               |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                        |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
