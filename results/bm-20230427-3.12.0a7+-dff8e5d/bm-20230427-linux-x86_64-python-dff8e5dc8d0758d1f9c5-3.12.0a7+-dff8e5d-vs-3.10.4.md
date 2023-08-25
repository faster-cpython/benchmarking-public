
# Results vs. 3.10.4

- fork: python
- ref: dff8e5dc8d0758d1f9c5
- machine: linux-x86_64
- commit hash: dff8e5d
- commit date: 2023-04-27
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 267 ms: 1.26x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.90 ms: 1.31x faster                                                  |
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                                 |
| html5lib       | 85.9 ms                                                | 64.9 ms: 1.32x faster                                                  |
| tornado_http   | 127 ms                                                 | 105 ms: 1.22x faster                                                   |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.9 ms: 1.59x faster                                                  |
| float          | 111 ms                                                 | 81.6 ms: 1.35x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.14x faster                                                  |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.79 ms: 1.17x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 316 us: 1.44x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 216 us: 1.39x faster                                                   |
| json_dumps           | 13.5 ms                                                | 10.1 ms: 1.34x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 58.6 ms: 1.28x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 84.7 ms: 1.11x faster                                                  |
| json_loads           | 28.8 us                                                | 25.9 us: 1.11x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                                   |
| unpickle_list        | 4.82 us                                                | 4.86 us: 1.01x slower                                                  |
| pickle_list          | 4.56 us                                                | 4.64 us: 1.02x slower                                                  |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                  |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                                  |
| pickle_dict          | 27.3 us                                                | 32.3 us: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.07 ms: 1.56x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.66 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                  |
| genshi_text     | 30.3 ms                                                | 22.4 ms: 1.35x faster                                                  |
| django_template | 45.9 ms                                                | 35.1 ms: 1.31x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 50.2 ms: 1.26x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7+-dff8e5d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.7 ms: 2.50x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.54 ms: 2.09x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 506 ms: 1.83x faster                                                   |
| richards                | 74.9 ms                                                | 43.7 ms: 1.71x faster                                                  |
| logging_silent          | 175 ns                                                 | 103 ns: 1.69x faster                                                   |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                                   |
| nbody                   | 142 ms                                                 | 88.9 ms: 1.59x faster                                                  |
| scimark_sor             | 197 ms                                                 | 126 ms: 1.56x faster                                                   |
| python_startup          | 14.2 ms                                                | 9.07 ms: 1.56x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.11 ms: 1.56x faster                                                  |
| chaos                   | 106 ms                                                 | 69.0 ms: 1.54x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.53x faster                                                  |
| raytrace                | 464 ms                                                 | 304 ms: 1.53x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 78.5 ms: 1.51x faster                                                  |
| pyflate                 | 673 ms                                                 | 450 ms: 1.49x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 72.8 ms: 1.49x faster                                                  |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.65 ms: 1.48x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 316 us: 1.44x faster                                                   |
| coroutines              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                  |
| spectral_norm           | 150 ms                                                 | 106 ms: 1.41x faster                                                   |
| unpickle_pure_python    | 300 us                                                 | 216 us: 1.39x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.38x faster                                                 |
| mako                    | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 47.3 ns: 1.37x faster                                                  |
| async_tree_none         | 717 ms                                                 | 529 ms: 1.36x faster                                                   |
| float                   | 111 ms                                                 | 81.6 ms: 1.35x faster                                                  |
| genshi_text             | 30.3 ms                                                | 22.4 ms: 1.35x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 38.9 us: 1.35x faster                                                  |
| json_dumps              | 13.5 ms                                                | 10.1 ms: 1.34x faster                                                  |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.33x faster                                                 |
| pprint_pformat          | 1.99 sec                                               | 1.49 sec: 1.33x faster                                                 |
| html5lib                | 85.9 ms                                                | 64.9 ms: 1.32x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 650 ms: 1.32x faster                                                   |
| chameleon               | 9.06 ms                                                | 6.90 ms: 1.31x faster                                                  |
| django_template         | 45.9 ms                                                | 35.1 ms: 1.31x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 731 ms: 1.31x faster                                                   |
| fannkuch                | 486 ms                                                 | 373 ms: 1.30x faster                                                   |
| thrift                  | 1.03 ms                                                | 801 us: 1.29x faster                                                   |
| logging_simple          | 8.07 us                                                | 6.26 us: 1.29x faster                                                  |
| logging_format          | 8.91 us                                                | 6.93 us: 1.29x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 58.6 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 749 ms: 1.27x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 50.2 ms: 1.26x faster                                                  |
| 2to3                    | 336 ms                                                 | 267 ms: 1.26x faster                                                   |
| nqueens                 | 100 ms                                                 | 81.3 ms: 1.23x faster                                                  |
| mypy2                   | 428 ms                                                 | 349 ms: 1.23x faster                                                   |
| regex_compile           | 177 ms                                                 | 145 ms: 1.22x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 111 ms: 1.22x faster                                                   |
| tornado_http            | 127 ms                                                 | 105 ms: 1.22x faster                                                   |
| deepcopy                | 442 us                                                 | 366 us: 1.21x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 3.18 us: 1.20x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 54.6 ms: 1.20x faster                                                  |
| scimark_fft             | 424 ms                                                 | 359 ms: 1.18x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.62 ms: 1.18x faster                                                  |
| docutils                | 3.17 sec                                               | 2.71 sec: 1.17x faster                                                 |
| comprehensions          | 26.8 us                                                | 23.2 us: 1.16x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 830 us: 1.14x faster                                                   |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.14x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 146 ms: 1.13x faster                                                   |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                  |
| pylint                  | 525 ms                                                 | 470 ms: 1.12x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 68.0 ms: 1.12x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.11x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 84.7 ms: 1.11x faster                                                  |
| json_loads              | 28.8 us                                                | 25.9 us: 1.11x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 21.8 ms: 1.11x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.4 ms: 1.09x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.59 sec: 1.09x faster                                                 |
| json                    | 5.42 ms                                                | 4.98 ms: 1.09x faster                                                  |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                                   |
| sympy_expand            | 545 ms                                                 | 503 ms: 1.08x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                                   |
| sqlite_synth            | 2.93 us                                                | 2.73 us: 1.08x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.08x faster                                                   |
| djangocms               | 35.9 us                                                | 33.7 us: 1.07x faster                                                  |
| sympy_str               | 328 ms                                                 | 309 ms: 1.06x faster                                                   |
| sympy_sum               | 185 ms                                                 | 180 ms: 1.02x faster                                                   |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                   |
| unpickle_list           | 4.82 us                                                | 4.86 us: 1.01x slower                                                  |
| pickle_list             | 4.56 us                                                | 4.64 us: 1.02x slower                                                  |
| gc_traversal            | 3.84 ms                                                | 3.95 ms: 1.03x slower                                                  |
| async_generators        | 425 ms                                                 | 440 ms: 1.03x slower                                                   |
| pickle                  | 10.3 us                                                | 10.7 us: 1.04x slower                                                  |
| unpickle                | 14.1 us                                                | 14.8 us: 1.05x slower                                                  |
| telco                   | 6.54 ms                                                | 6.89 ms: 1.05x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.66 ms: 1.14x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.79 ms: 1.17x slower                                                  |
| pickle_dict             | 27.3 us                                                | 32.3 us: 1.19x slower                                                  |
| dask                    | 423 ms                                                 | 538 ms: 1.27x slower                                                   |
| coverage                | 72.8 ms                                                | 101 ms: 1.39x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (2): meteor_contest, bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x
