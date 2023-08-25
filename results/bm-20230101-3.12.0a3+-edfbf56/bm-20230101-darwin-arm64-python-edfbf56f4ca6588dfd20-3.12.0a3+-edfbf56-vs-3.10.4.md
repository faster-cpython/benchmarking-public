
# Results vs. 3.10.4

- fork: python
- ref: edfbf56f4ca6588dfd20
- machine: darwin-arm64
- commit hash: edfbf56
- commit date: 2023-01-01
- overall geometric mean: 1.22x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 163 ms: 1.24x faster                                                   |
| chameleon      | 5.84 ms                                                | 4.56 ms: 1.28x faster                                                  |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                 |
| html5lib       | 44.1 ms                                                | 34.1 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 63.8 ms: 1.47x faster                                                  |
| float          | 72.3 ms                                                | 51.6 ms: 1.40x faster                                                  |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 74.9 ms: 1.29x faster                                                  |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                  |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                                   |
| regex_effbot   | 2.45 ms                                                | 2.60 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 193 us: 1.47x faster                                                   |
| unpickle_pure_python | 203 us                                                 | 142 us: 1.44x faster                                                   |
| json_dumps           | 8.38 ms                                                | 6.13 ms: 1.37x faster                                                  |
| xml_etree_process    | 45.1 ms                                                | 35.2 ms: 1.28x faster                                                  |
| xml_etree_generate   | 54.3 ms                                                | 48.5 ms: 1.12x faster                                                  |
| xml_etree_parse      | 107 ms                                                 | 96.5 ms: 1.11x faster                                                  |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 69.9 ms: 1.04x faster                                                  |
| unpickle             | 9.77 us                                                | 9.63 us: 1.01x faster                                                  |
| pickle_list          | 2.83 us                                                | 2.84 us: 1.01x slower                                                  |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                                  |
| pickle               | 7.36 us                                                | 7.46 us: 1.01x slower                                                  |
| unpickle_list        | 2.66 us                                                | 2.70 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.3 ms: 1.02x faster                                                  |
| python_startup_no_site | 9.73 ms                                                | 10.3 ms: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 37.6 ms                                                | 28.4 ms: 1.33x faster                                                  |
| mako            | 10.5 ms                                                | 8.15 ms: 1.29x faster                                                  |
| django_template | 27.3 ms                                                | 22.0 ms: 1.24x faster                                                  |
| genshi_text     | 18.4 ms                                                | 15.0 ms: 1.23x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.62 ms: 1.97x faster                                                  |
| logging_silent          | 119 ns                                                 | 64.7 ns: 1.84x faster                                                  |
| richards                | 51.4 ms                                                | 30.4 ms: 1.69x faster                                                  |
| scimark_sor             | 127 ms                                                 | 80.3 ms: 1.58x faster                                                  |
| scimark_lu              | 110 ms                                                 | 71.8 ms: 1.53x faster                                                  |
| go                      | 165 ms                                                 | 108 ms: 1.53x faster                                                   |
| raytrace                | 328 ms                                                 | 217 ms: 1.51x faster                                                   |
| async_tree_memoization  | 493 ms                                                 | 333 ms: 1.48x faster                                                   |
| nbody                   | 94.1 ms                                                | 63.8 ms: 1.47x faster                                                  |
| asyncio_tcp             | 673 ms                                                 | 457 ms: 1.47x faster                                                   |
| pickle_pure_python      | 284 us                                                 | 193 us: 1.47x faster                                                   |
| crypto_pyaes            | 78.0 ms                                                | 53.8 ms: 1.45x faster                                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 49.8 ms: 1.45x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 142 us: 1.44x faster                                                   |
| float                   | 72.3 ms                                                | 51.6 ms: 1.40x faster                                                  |
| pyflate                 | 453 ms                                                 | 325 ms: 1.40x faster                                                   |
| async_tree_none         | 402 ms                                                 | 289 ms: 1.39x faster                                                   |
| json_dumps              | 8.38 ms                                                | 6.13 ms: 1.37x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 750 ms: 1.36x faster                                                   |
| pycparser               | 915 ms                                                 | 678 ms: 1.35x faster                                                   |
| deepcopy_memo           | 34.5 us                                                | 25.8 us: 1.34x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.47 us: 1.33x faster                                                  |
| logging_format          | 5.01 us                                                | 3.76 us: 1.33x faster                                                  |
| thrift                  | 586 us                                                 | 441 us: 1.33x faster                                                   |
| genshi_xml              | 37.6 ms                                                | 28.4 ms: 1.33x faster                                                  |
| pprint_pformat          | 1.24 sec                                               | 936 ms: 1.33x faster                                                   |
| pprint_safe_repr        | 609 ms                                                 | 460 ms: 1.32x faster                                                   |
| chaos                   | 66.8 ms                                                | 51.0 ms: 1.31x faster                                                  |
| spectral_norm           | 96.4 ms                                                | 74.2 ms: 1.30x faster                                                  |
| html5lib                | 44.1 ms                                                | 34.1 ms: 1.29x faster                                                  |
| regex_compile           | 96.6 ms                                                | 74.9 ms: 1.29x faster                                                  |
| sqlglot_parse           | 1.33 ms                                                | 1.03 ms: 1.29x faster                                                  |
| mako                    | 10.5 ms                                                | 8.15 ms: 1.29x faster                                                  |
| sqlglot_transpile       | 1.54 ms                                                | 1.20 ms: 1.28x faster                                                  |
| chameleon               | 5.84 ms                                                | 4.56 ms: 1.28x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.93 ms: 1.28x faster                                                  |
| xml_etree_process       | 45.1 ms                                                | 35.2 ms: 1.28x faster                                                  |
| create_gc_cycles        | 876 us                                                 | 695 us: 1.26x faster                                                   |
| deepcopy                | 278 us                                                 | 221 us: 1.26x faster                                                   |
| deepcopy_reduce         | 2.38 us                                                | 1.90 us: 1.25x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.6 ms: 1.25x faster                                                  |
| 2to3                    | 202 ms                                                 | 163 ms: 1.24x faster                                                   |
| django_template         | 27.3 ms                                                | 22.0 ms: 1.24x faster                                                  |
| fannkuch                | 317 ms                                                 | 257 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed | 670 ms                                                 | 543 ms: 1.23x faster                                                   |
| genshi_text             | 18.4 ms                                                | 15.0 ms: 1.23x faster                                                  |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.85 ms: 1.22x faster                                                  |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.8 ms: 1.20x faster                                                  |
| unpack_sequence         | 38.7 ns                                                | 32.7 ns: 1.18x faster                                                  |
| bench_thread_pool       | 548 us                                                 | 465 us: 1.18x faster                                                   |
| scimark_fft             | 232 ms                                                 | 198 ms: 1.17x faster                                                   |
| mypy2                   | 308 ms                                                 | 264 ms: 1.17x faster                                                   |
| async_generators        | 233 ms                                                 | 201 ms: 1.16x faster                                                   |
| sympy_integrate         | 13.4 ms                                                | 11.5 ms: 1.16x faster                                                  |
| dask                    | 258 ms                                                 | 226 ms: 1.14x faster                                                   |
| sympy_expand            | 276 ms                                                 | 245 ms: 1.12x faster                                                   |
| sqlglot_normalize       | 197 ms                                                 | 175 ms: 1.12x faster                                                   |
| xml_etree_generate      | 54.3 ms                                                | 48.5 ms: 1.12x faster                                                  |
| coroutines              | 20.2 ms                                                | 18.1 ms: 1.12x faster                                                  |
| regex_v8                | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                  |
| json                    | 3.10 ms                                                | 2.78 ms: 1.11x faster                                                  |
| xml_etree_parse         | 107 ms                                                 | 96.5 ms: 1.11x faster                                                  |
| nqueens                 | 68.1 ms                                                | 61.6 ms: 1.11x faster                                                  |
| sympy_str               | 169 ms                                                 | 153 ms: 1.10x faster                                                   |
| sqlite_synth            | 1.47 us                                                | 1.34 us: 1.10x faster                                                  |
| sympy_sum               | 94.3 ms                                                | 86.1 ms: 1.10x faster                                                  |
| mdp                     | 1.67 sec                                               | 1.53 sec: 1.09x faster                                                 |
| regex_dna               | 160 ms                                                 | 149 ms: 1.07x faster                                                   |
| pathlib                 | 28.8 ms                                                | 27.4 ms: 1.05x faster                                                  |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                                  |
| telco                   | 3.68 ms                                                | 3.54 ms: 1.04x faster                                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 69.9 ms: 1.04x faster                                                  |
| meteor_contest          | 78.6 ms                                                | 76.4 ms: 1.03x faster                                                  |
| python_startup          | 12.6 ms                                                | 12.3 ms: 1.02x faster                                                  |
| unpickle                | 9.77 us                                                | 9.63 us: 1.01x faster                                                  |
| pidigits                | 282 ms                                                 | 280 ms: 1.01x faster                                                   |
| pickle_list             | 2.83 us                                                | 2.84 us: 1.01x slower                                                  |
| gc_traversal            | 2.40 ms                                                | 2.42 ms: 1.01x slower                                                  |
| generators              | 32.9 ms                                                | 33.2 ms: 1.01x slower                                                  |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                                  |
| comprehensions          | 17.7 us                                                | 17.9 us: 1.01x slower                                                  |
| pickle                  | 7.36 us                                                | 7.46 us: 1.01x slower                                                  |
| unpickle_list           | 2.66 us                                                | 2.70 us: 1.02x slower                                                  |
| python_startup_no_site  | 9.73 ms                                                | 10.3 ms: 1.06x slower                                                  |
| regex_effbot            | 2.45 ms                                                | 2.60 ms: 1.07x slower                                                  |
| bench_mp_pool           | 41.0 ms                                                | 44.3 ms: 1.08x slower                                                  |
| coverage                | 40.8 ms                                                | 54.6 ms: 1.34x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.22x faster                                                           |
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x
