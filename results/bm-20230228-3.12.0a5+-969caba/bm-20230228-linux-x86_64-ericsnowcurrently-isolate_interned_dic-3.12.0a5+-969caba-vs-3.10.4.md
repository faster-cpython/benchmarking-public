
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: isolate_interned_dic
- machine: linux-x86_64
- commit hash: 969caba
- commit date: 2023-02-28
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                              |
| chameleon      | 9.06 ms                                                | 6.44 ms: 1.41x faster                                                             |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                            |
| html5lib       | 85.9 ms                                                | 62.0 ms: 1.39x faster                                                             |
| tornado_http   | 127 ms                                                 | 95.3 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.4 ms: 1.53x faster                                                             |
| float          | 111 ms                                                 | 73.4 ms: 1.50x faster                                                             |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                             |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.67 ms: 1.14x slower                                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 293 us: 1.55x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 203 us: 1.48x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.47 ms: 1.43x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 56.1 ms: 1.33x faster                                                             |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 81.4 ms: 1.16x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 99.0 ms: 1.13x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                              |
| pickle_list          | 4.56 us                                                | 4.17 us: 1.09x faster                                                             |
| unpickle             | 14.1 us                                                | 13.5 us: 1.05x faster                                                             |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                             |
| unpickle_list        | 4.82 us                                                | 5.01 us: 1.04x slower                                                             |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.00 ms: 1.57x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.93 ms: 1.49x faster                                                             |
| genshi_text     | 30.3 ms                                                | 21.7 ms: 1.40x faster                                                             |
| django_template | 45.9 ms                                                | 33.9 ms: 1.35x faster                                                             |
| genshi_xml      | 63.3 ms                                                | 48.7 ms: 1.30x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.7 ms: 2.50x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.25 ms: 2.29x faster                                                             |
| logging_silent          | 175 ns                                                 | 93.8 ns: 1.87x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 499 ms: 1.86x faster                                                              |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.83x faster                                                              |
| richards                | 74.9 ms                                                | 44.3 ms: 1.69x faster                                                             |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                                              |
| pyflate                 | 673 ms                                                 | 413 ms: 1.63x faster                                                              |
| scimark_monte_carlo     | 108 ms                                                 | 66.7 ms: 1.62x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 73.9 ms: 1.60x faster                                                             |
| raytrace                | 464 ms                                                 | 293 ms: 1.58x faster                                                              |
| chaos                   | 106 ms                                                 | 67.2 ms: 1.58x faster                                                             |
| python_startup          | 14.2 ms                                                | 9.00 ms: 1.57x faster                                                             |
| spectral_norm           | 150 ms                                                 | 95.8 ms: 1.56x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 293 us: 1.55x faster                                                              |
| unpack_sequence         | 64.7 ns                                                | 41.9 ns: 1.55x faster                                                             |
| nbody                   | 142 ms                                                 | 92.4 ms: 1.53x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.25 ms: 1.52x faster                                                             |
| deepcopy_memo           | 52.3 us                                                | 34.6 us: 1.51x faster                                                             |
| float                   | 111 ms                                                 | 73.4 ms: 1.50x faster                                                             |
| mako                    | 14.8 ms                                                | 9.93 ms: 1.49x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 203 us: 1.48x faster                                                              |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                                              |
| json_dumps              | 13.5 ms                                                | 9.47 ms: 1.43x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.45 ms: 1.42x faster                                                             |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                                            |
| chameleon               | 9.06 ms                                                | 6.44 ms: 1.41x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.75 ms: 1.40x faster                                                             |
| genshi_text             | 30.3 ms                                                | 21.7 ms: 1.40x faster                                                             |
| pprint_safe_repr        | 955 ms                                                 | 686 ms: 1.39x faster                                                              |
| logging_format          | 8.91 us                                                | 6.41 us: 1.39x faster                                                             |
| html5lib                | 85.9 ms                                                | 62.0 ms: 1.39x faster                                                             |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                             |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                                              |
| logging_simple          | 8.07 us                                                | 5.89 us: 1.37x faster                                                             |
| scimark_fft             | 424 ms                                                 | 310 ms: 1.37x faster                                                              |
| coroutines              | 31.8 ms                                                | 23.3 ms: 1.36x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                                            |
| django_template         | 45.9 ms                                                | 33.9 ms: 1.35x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                                            |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                             |
| tornado_http            | 127 ms                                                 | 95.3 ms: 1.34x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 56.1 ms: 1.33x faster                                                             |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                              |
| fannkuch                | 486 ms                                                 | 365 ms: 1.33x faster                                                              |
| thrift                  | 1.03 ms                                                | 781 us: 1.32x faster                                                              |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                              |
| deepcopy                | 442 us                                                 | 339 us: 1.30x faster                                                              |
| genshi_xml              | 63.3 ms                                                | 48.7 ms: 1.30x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 659 ms: 1.30x faster                                                              |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                              |
| async_tree_cpu_io_mixed | 951 ms                                                 | 742 ms: 1.28x faster                                                              |
| mypy2                   | 428 ms                                                 | 335 ms: 1.28x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                | 51.3 ms: 1.27x faster                                                             |
| deepcopy_reduce         | 3.82 us                                                | 3.02 us: 1.27x faster                                                             |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                            |
| nqueens                 | 100 ms                                                 | 81.1 ms: 1.23x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.56 ms: 1.20x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 798 us: 1.19x faster                                                              |
| dulwich_log             | 75.9 ms                                                | 64.0 ms: 1.19x faster                                                             |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                                             |
| sympy_integrate         | 24.3 ms                                                | 20.7 ms: 1.17x faster                                                             |
| sympy_expand            | 545 ms                                                 | 469 ms: 1.16x faster                                                              |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.2 ms: 1.16x faster                                                             |
| json                    | 5.42 ms                                                | 4.68 ms: 1.16x faster                                                             |
| xml_etree_generate      | 94.2 ms                                                | 81.4 ms: 1.16x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.47 sec: 1.14x faster                                                            |
| sympy_str               | 328 ms                                                 | 289 ms: 1.14x faster                                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                             |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 99.0 ms: 1.13x faster                                                             |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                             |
| comprehensions          | 26.8 us                                                | 24.0 us: 1.12x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                              |
| djangocms               | 35.9 us                                                | 32.8 us: 1.10x faster                                                             |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                                              |
| sympy_sum               | 185 ms                                                 | 169 ms: 1.09x faster                                                              |
| pickle_list             | 4.56 us                                                | 4.17 us: 1.09x faster                                                             |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                                              |
| unpickle                | 14.1 us                                                | 13.5 us: 1.05x faster                                                             |
| telco                   | 6.54 ms                                                | 6.34 ms: 1.03x faster                                                             |
| async_generators        | 425 ms                                                 | 418 ms: 1.02x faster                                                              |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                                             |
| unpickle_list           | 4.82 us                                                | 5.01 us: 1.04x slower                                                             |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                              |
| gc_traversal            | 3.84 ms                                                | 4.31 ms: 1.12x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.67 ms: 1.14x slower                                                             |
| pickle_dict             | 27.3 us                                                | 31.6 us: 1.16x slower                                                             |
| dask                    | 423 ms                                                 | 511 ms: 1.21x slower                                                              |
| coverage                | 72.8 ms                                                | 96.7 ms: 1.33x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
