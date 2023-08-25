
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 206f05a
- commit date: 2023-01-14
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 183 ms: 1.11x faster                                   |
| chameleon      | 5.84 ms                                                | 4.59 ms: 1.27x faster                                  |
| docutils       | 1.78 sec                                               | 1.44 sec: 1.23x faster                                 |
| html5lib       | 44.1 ms                                                | 34.7 ms: 1.27x faster                                  |
| tornado_http   | 91.9 ms                                                | 68.3 ms: 1.35x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 63.4 ms: 1.49x faster                                  |
| float          | 72.3 ms                                                | 51.5 ms: 1.41x faster                                  |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 74.6 ms: 1.30x faster                                  |
| regex_v8       | 17.5 ms                                                | 16.8 ms: 1.04x faster                                  |
| regex_dna      | 160 ms                                                 | 154 ms: 1.04x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.73 ms: 1.12x slower                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 194 us: 1.46x faster                                   |
| unpickle_pure_python | 203 us                                                 | 142 us: 1.43x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.12 ms: 1.37x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 34.8 ms: 1.30x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 93.1 ms: 1.15x faster                                  |
| xml_etree_generate   | 54.3 ms                                                | 48.0 ms: 1.13x faster                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 66.4 ms: 1.09x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| unpickle             | 9.77 us                                                | 9.84 us: 1.01x slower                                  |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| unpickle_list        | 2.66 us                                                | 2.71 us: 1.02x slower                                  |
| pickle_list          | 2.83 us                                                | 2.89 us: 1.02x slower                                  |
| pickle               | 7.36 us                                                | 7.56 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 9.33 ms: 1.35x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 7.34 ms: 1.33x faster                                  |
| Geometric mean         | (ref)                                                  | 1.34x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 37.6 ms                                                | 28.4 ms: 1.32x faster                                  |
| mako            | 10.5 ms                                                | 8.10 ms: 1.29x faster                                  |
| django_template | 27.3 ms                                                | 21.7 ms: 1.26x faster                                  |
| genshi_text     | 18.4 ms                                                | 15.2 ms: 1.21x faster                                  |
| Geometric mean  | (ref)                                                  | 1.27x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.61 ms: 1.97x faster                                  |
| logging_silent          | 119 ns                                                 | 66.2 ns: 1.80x faster                                  |
| richards                | 51.4 ms                                                | 30.4 ms: 1.69x faster                                  |
| asyncio_tcp             | 673 ms                                                 | 408 ms: 1.65x faster                                   |
| scimark_sor             | 127 ms                                                 | 82.0 ms: 1.54x faster                                  |
| go                      | 165 ms                                                 | 108 ms: 1.52x faster                                   |
| scimark_lu              | 110 ms                                                 | 72.3 ms: 1.52x faster                                  |
| async_tree_memoization  | 493 ms                                                 | 327 ms: 1.51x faster                                   |
| nbody                   | 94.1 ms                                                | 63.4 ms: 1.49x faster                                  |
| crypto_pyaes            | 78.0 ms                                                | 52.9 ms: 1.47x faster                                  |
| raytrace                | 328 ms                                                 | 223 ms: 1.47x faster                                   |
| pickle_pure_python      | 284 us                                                 | 194 us: 1.46x faster                                   |
| unpickle_pure_python    | 203 us                                                 | 142 us: 1.43x faster                                   |
| scimark_monte_carlo     | 72.2 ms                                                | 50.6 ms: 1.43x faster                                  |
| pyflate                 | 453 ms                                                 | 319 ms: 1.42x faster                                   |
| async_tree_none         | 402 ms                                                 | 285 ms: 1.41x faster                                   |
| float                   | 72.3 ms                                                | 51.5 ms: 1.41x faster                                  |
| async_tree_io           | 1.02 sec                                               | 737 ms: 1.38x faster                                   |
| pathlib                 | 28.8 ms                                                | 20.9 ms: 1.38x faster                                  |
| json_dumps              | 8.38 ms                                                | 6.12 ms: 1.37x faster                                  |
| python_startup          | 12.6 ms                                                | 9.33 ms: 1.35x faster                                  |
| tornado_http            | 91.9 ms                                                | 68.3 ms: 1.35x faster                                  |
| pycparser               | 915 ms                                                 | 682 ms: 1.34x faster                                   |
| deepcopy_memo           | 34.5 us                                                | 25.9 us: 1.33x faster                                  |
| chaos                   | 66.8 ms                                                | 50.3 ms: 1.33x faster                                  |
| thrift                  | 586 us                                                 | 442 us: 1.33x faster                                   |
| python_startup_no_site  | 9.73 ms                                                | 7.34 ms: 1.33x faster                                  |
| genshi_xml              | 37.6 ms                                                | 28.4 ms: 1.32x faster                                  |
| logging_format          | 5.01 us                                                | 3.79 us: 1.32x faster                                  |
| logging_simple          | 4.63 us                                                | 3.50 us: 1.32x faster                                  |
| pprint_pformat          | 1.24 sec                                               | 939 ms: 1.32x faster                                   |
| pprint_safe_repr        | 609 ms                                                 | 464 ms: 1.31x faster                                   |
| spectral_norm           | 96.4 ms                                                | 73.6 ms: 1.31x faster                                  |
| sqlglot_parse           | 1.33 ms                                                | 1.02 ms: 1.30x faster                                  |
| dulwich_log             | 37.1 ms                                                | 28.6 ms: 1.30x faster                                  |
| sqlglot_transpile       | 1.54 ms                                                | 1.18 ms: 1.30x faster                                  |
| regex_compile           | 96.6 ms                                                | 74.6 ms: 1.30x faster                                  |
| xml_etree_process       | 45.1 ms                                                | 34.8 ms: 1.30x faster                                  |
| mako                    | 10.5 ms                                                | 8.10 ms: 1.29x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.92 ms: 1.28x faster                                  |
| chameleon               | 5.84 ms                                                | 4.59 ms: 1.27x faster                                  |
| html5lib                | 44.1 ms                                                | 34.7 ms: 1.27x faster                                  |
| create_gc_cycles        | 876 us                                                 | 690 us: 1.27x faster                                   |
| django_template         | 27.3 ms                                                | 21.7 ms: 1.26x faster                                  |
| deepcopy                | 278 us                                                 | 220 us: 1.26x faster                                   |
| deepcopy_reduce         | 2.38 us                                                | 1.90 us: 1.26x faster                                  |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.79 ms: 1.24x faster                                  |
| fannkuch                | 317 ms                                                 | 255 ms: 1.24x faster                                   |
| async_tree_cpu_io_mixed | 670 ms                                                 | 540 ms: 1.24x faster                                   |
| docutils                | 1.78 sec                                               | 1.44 sec: 1.23x faster                                 |
| bench_thread_pool       | 548 us                                                 | 447 us: 1.23x faster                                   |
| sqlglot_optimize        | 38.0 ms                                                | 31.2 ms: 1.22x faster                                  |
| genshi_text             | 18.4 ms                                                | 15.2 ms: 1.21x faster                                  |
| scimark_fft             | 232 ms                                                 | 195 ms: 1.19x faster                                   |
| unpack_sequence         | 38.7 ns                                                | 32.8 ns: 1.18x faster                                  |
| sympy_integrate         | 13.4 ms                                                | 11.4 ms: 1.17x faster                                  |
| async_generators        | 233 ms                                                 | 200 ms: 1.17x faster                                   |
| xml_etree_parse         | 107 ms                                                 | 93.1 ms: 1.15x faster                                  |
| sqlglot_normalize       | 197 ms                                                 | 171 ms: 1.15x faster                                   |
| sympy_expand            | 276 ms                                                 | 241 ms: 1.14x faster                                   |
| xml_etree_generate      | 54.3 ms                                                | 48.0 ms: 1.13x faster                                  |
| nqueens                 | 68.1 ms                                                | 60.8 ms: 1.12x faster                                  |
| sympy_str               | 169 ms                                                 | 151 ms: 1.12x faster                                   |
| mdp                     | 1.67 sec                                               | 1.50 sec: 1.11x faster                                 |
| 2to3                    | 202 ms                                                 | 183 ms: 1.11x faster                                   |
| sympy_sum               | 94.3 ms                                                | 85.9 ms: 1.10x faster                                  |
| json                    | 3.10 ms                                                | 2.82 ms: 1.10x faster                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 66.4 ms: 1.09x faster                                  |
| telco                   | 3.68 ms                                                | 3.39 ms: 1.09x faster                                  |
| coroutines              | 20.2 ms                                                | 18.6 ms: 1.08x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.38 us: 1.07x faster                                  |
| meteor_contest          | 78.6 ms                                                | 74.5 ms: 1.06x faster                                  |
| regex_v8                | 17.5 ms                                                | 16.8 ms: 1.04x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| regex_dna               | 160 ms                                                 | 154 ms: 1.04x faster                                   |
| pidigits                | 282 ms                                                 | 282 ms: 1.00x slower                                   |
| gc_traversal            | 2.40 ms                                                | 2.41 ms: 1.00x slower                                  |
| unpickle                | 9.77 us                                                | 9.84 us: 1.01x slower                                  |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| unpickle_list           | 2.66 us                                                | 2.71 us: 1.02x slower                                  |
| generators              | 32.9 ms                                                | 33.6 ms: 1.02x slower                                  |
| pickle_list             | 2.83 us                                                | 2.89 us: 1.02x slower                                  |
| bench_mp_pool           | 41.0 ms                                                | 42.1 ms: 1.03x slower                                  |
| pickle                  | 7.36 us                                                | 7.56 us: 1.03x slower                                  |
| regex_effbot            | 2.45 ms                                                | 2.73 ms: 1.12x slower                                  |
| dask                    | 258 ms                                                 | 321 ms: 1.25x slower                                   |
| coverage                | 40.8 ms                                                | 56.4 ms: 1.38x slower                                  |
| Geometric mean          | (ref)                                                  | 1.23x faster                                           |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230114-3.12.0a4+-206f05a/bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x
