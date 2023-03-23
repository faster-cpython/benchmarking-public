
# Results vs. 3.10.4

- fork: python
- ref: edfbf56f4ca6588dfd20
- machine: darwin-arm64
- commit hash: edfbf56
- commit date: 2023-01-01
- overall geometric mean: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 163 ms: 1.23x faster                                                   |
| chameleon      | 5.79 ms                                                | 4.56 ms: 1.27x faster                                                  |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.21x faster                                                 |
| html5lib       | 44.2 ms                                                | 34.1 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 63.8 ms: 1.46x faster                                                  |
| float          | 72.4 ms                                                | 51.6 ms: 1.40x faster                                                  |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 74.9 ms: 1.29x faster                                                  |
| regex_v8       | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.60 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 193 us: 1.47x faster                                                   |
| unpickle_pure_python | 203 us                                                 | 142 us: 1.43x faster                                                   |
| json_dumps           | 8.40 ms                                                | 6.13 ms: 1.37x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 35.2 ms: 1.27x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.5 ms: 1.12x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 96.5 ms: 1.10x faster                                                  |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 69.9 ms: 1.03x faster                                                  |
| unpickle             | 9.89 us                                                | 9.63 us: 1.03x faster                                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                                  |
| unpickle_list        | 2.69 us                                                | 2.70 us: 1.01x slower                                                  |
| pickle_list          | 2.80 us                                                | 2.84 us: 1.01x slower                                                  |
| pickle               | 7.35 us                                                | 7.46 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.3 ms: 1.04x slower                                                  |
| python_startup_no_site | 8.88 ms                                                | 10.3 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 37.2 ms                                                | 28.4 ms: 1.31x faster                                                  |
| mako            | 10.5 ms                                                | 8.15 ms: 1.29x faster                                                  |
| django_template | 27.3 ms                                                | 22.0 ms: 1.24x faster                                                  |
| genshi_text     | 18.4 ms                                                | 15.0 ms: 1.23x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-darwin-arm64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.62 ms: 1.97x faster                                                  |
| logging_silent          | 119 ns                                                 | 64.7 ns: 1.84x faster                                                  |
| richards                | 51.4 ms                                                | 30.4 ms: 1.69x faster                                                  |
| scimark_sor             | 126 ms                                                 | 80.3 ms: 1.57x faster                                                  |
| go                      | 165 ms                                                 | 108 ms: 1.54x faster                                                   |
| scimark_lu              | 109 ms                                                 | 71.8 ms: 1.52x faster                                                  |
| raytrace                | 325 ms                                                 | 217 ms: 1.50x faster                                                   |
| async_tree_memoization  | 490 ms                                                 | 333 ms: 1.47x faster                                                   |
| pickle_pure_python      | 283 us                                                 | 193 us: 1.47x faster                                                   |
| asyncio_tcp             | 670 ms                                                 | 457 ms: 1.46x faster                                                   |
| nbody                   | 93.3 ms                                                | 63.8 ms: 1.46x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 49.8 ms: 1.45x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 53.8 ms: 1.45x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 142 us: 1.43x faster                                                   |
| float                   | 72.4 ms                                                | 51.6 ms: 1.40x faster                                                  |
| pyflate                 | 453 ms                                                 | 325 ms: 1.40x faster                                                   |
| async_tree_none         | 400 ms                                                 | 289 ms: 1.39x faster                                                   |
| json_dumps              | 8.40 ms                                                | 6.13 ms: 1.37x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 750 ms: 1.36x faster                                                   |
| pycparser               | 916 ms                                                 | 678 ms: 1.35x faster                                                   |
| deepcopy_memo           | 34.4 us                                                | 25.8 us: 1.33x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.47 us: 1.33x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.03 ms: 1.32x faster                                                  |
| logging_format          | 4.97 us                                                | 3.76 us: 1.32x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 460 ms: 1.32x faster                                                   |
| pprint_pformat          | 1.23 sec                                               | 936 ms: 1.32x faster                                                   |
| thrift                  | 580 us                                                 | 441 us: 1.32x faster                                                   |
| sqlglot_transpile       | 1.57 ms                                                | 1.20 ms: 1.31x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 28.4 ms: 1.31x faster                                                  |
| chaos                   | 66.7 ms                                                | 51.0 ms: 1.31x faster                                                  |
| html5lib                | 44.2 ms                                                | 34.1 ms: 1.29x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 74.2 ms: 1.29x faster                                                  |
| regex_compile           | 96.4 ms                                                | 74.9 ms: 1.29x faster                                                  |
| mako                    | 10.5 ms                                                | 8.15 ms: 1.29x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.93 ms: 1.28x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 35.2 ms: 1.27x faster                                                  |
| deepcopy                | 281 us                                                 | 221 us: 1.27x faster                                                   |
| chameleon               | 5.79 ms                                                | 4.56 ms: 1.27x faster                                                  |
| create_gc_cycles        | 880 us                                                 | 695 us: 1.27x faster                                                   |
| dulwich_log             | 37.1 ms                                                | 29.6 ms: 1.25x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.90 us: 1.25x faster                                                  |
| django_template         | 27.3 ms                                                | 22.0 ms: 1.24x faster                                                  |
| fannkuch                | 317 ms                                                 | 257 ms: 1.24x faster                                                   |
| 2to3                    | 201 ms                                                 | 163 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed | 669 ms                                                 | 543 ms: 1.23x faster                                                   |
| genshi_text             | 18.4 ms                                                | 15.0 ms: 1.23x faster                                                  |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.21x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.85 ms: 1.21x faster                                                  |
| sqlglot_optimize        | 38.0 ms                                                | 31.8 ms: 1.20x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 465 us: 1.17x faster                                                   |
| dask                    | 265 ms                                                 | 226 ms: 1.17x faster                                                   |
| scimark_fft             | 230 ms                                                 | 198 ms: 1.17x faster                                                   |
| async_generators        | 234 ms                                                 | 201 ms: 1.16x faster                                                   |
| mypy2                   | 307 ms                                                 | 264 ms: 1.16x faster                                                   |
| sympy_integrate         | 13.3 ms                                                | 11.5 ms: 1.15x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 32.7 ns: 1.14x faster                                                  |
| sympy_expand            | 275 ms                                                 | 245 ms: 1.12x faster                                                   |
| sqlglot_normalize       | 196 ms                                                 | 175 ms: 1.12x faster                                                   |
| regex_v8                | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 48.5 ms: 1.12x faster                                                  |
| coroutines              | 20.2 ms                                                | 18.1 ms: 1.11x faster                                                  |
| json                    | 3.08 ms                                                | 2.78 ms: 1.11x faster                                                  |
| nqueens                 | 68.2 ms                                                | 61.6 ms: 1.11x faster                                                  |
| sympy_str               | 169 ms                                                 | 153 ms: 1.10x faster                                                   |
| xml_etree_parse         | 106 ms                                                 | 96.5 ms: 1.10x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.34 us: 1.10x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 86.1 ms: 1.09x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.53 sec: 1.08x faster                                                 |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| pathlib                 | 28.8 ms                                                | 27.4 ms: 1.05x faster                                                  |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 69.9 ms: 1.03x faster                                                  |
| telco                   | 3.63 ms                                                | 3.54 ms: 1.03x faster                                                  |
| unpickle                | 9.89 us                                                | 9.63 us: 1.03x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 76.4 ms: 1.02x faster                                                  |
| pidigits                | 282 ms                                                 | 280 ms: 1.01x faster                                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                  |
| unpickle_list           | 2.69 us                                                | 2.70 us: 1.01x slower                                                  |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                                  |
| pickle_list             | 2.80 us                                                | 2.84 us: 1.01x slower                                                  |
| pickle                  | 7.35 us                                                | 7.46 us: 1.02x slower                                                  |
| generators              | 32.7 ms                                                | 33.2 ms: 1.02x slower                                                  |
| comprehensions          | 17.6 us                                                | 17.9 us: 1.02x slower                                                  |
| python_startup          | 11.9 ms                                                | 12.3 ms: 1.04x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.60 ms: 1.06x slower                                                  |
| bench_mp_pool           | 39.7 ms                                                | 44.3 ms: 1.12x slower                                                  |
| python_startup_no_site  | 8.88 ms                                                | 10.3 ms: 1.16x slower                                                  |
| coverage                | 42.0 ms                                                | 54.6 ms: 1.30x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                           |
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
